import os
import tempfile
import unittest

os.environ["DB_PATH"] = tempfile.mktemp(suffix=".db")

from app import app, init, classify, recommend_package, score, score_breakdown


class InteriorFlowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init()

    def setUp(self):
        self.client = app.test_client()
        self.client.post("/api/auth/login", json={"username": "demo", "password": "demo"})

    def test_lead_creation_duplicate_and_state(self):
        data = {"name": "Test Customer", "email": "test@example.com", "budget": 12,
                "timeline": 30, "location": "Hyderabad", "property": "3 BHK", "consent": True}
        created = self.client.post("/api/leads", json=data)
        self.assertEqual(created.status_code, 201)
        self.assertEqual(created.json["score"], 100)
        self.assertEqual(created.json["classification"], "Hot")
        self.assertEqual(self.client.post("/api/leads", json=data).status_code, 409)
        state = self.client.get("/api/state").json
        self.assertGreaterEqual(state["metrics"]["total_leads"], 31)

    def test_invalid_lead_fields(self):
        self.assertEqual(self.client.post("/api/leads", json={}).status_code, 400)
        self.assertEqual(self.client.post("/api/leads", json={
            "name": "", "email": "bad", "budget": -1, "timeline": 0,
            "location": "", "property": ""
        }).status_code, 400)

    def test_score_classification_boundaries(self):
        self.assertEqual(classify(79), "Warm")
        self.assertEqual(classify(80), "Hot")
        self.assertEqual(classify(49), "Cold")
        self.assertEqual(classify(50), "Warm")

    def test_score_breakdown(self):
        hot = score_breakdown(12, 30, "Hyderabad", "Complete modular kitchen and living room renovation", True)
        cold = score_breakdown(2, 180, "Mumbai", "", False)
        self.assertGreater(hot["total"], cold["total"])
        self.assertEqual(hot["total"], 100)

    def test_package_recommendations_are_labelled(self):
        package = recommend_package(12, "3 BHK")
        self.assertIn("verify", package.lower())
        self.assertIn("Platinum", package)

    def test_consent_creates_followups(self):
        data = {"name": "Consent Demo", "email": "consent@example.com", "budget": 7,
                "timeline": 45, "location": "Miyapur", "property": "3 BHK", "consent": True}
        created = self.client.post("/api/leads", json=data)
        lead_id = created.json["id"]
        state = self.client.get("/api/state").json
        followups = [row for row in state["followups"] if row["lead_id"] == lead_id]
        self.assertEqual(len(followups), 4)

    def test_no_consent_no_followup(self):
        data = {"name": "No Consent", "email": "noconsent@example.com", "budget": 6,
                "timeline": 60, "location": "Kondapur", "property": "2 BHK", "consent": False}
        created = self.client.post("/api/leads", json=data)
        lead_id = created.json["id"]
        state = self.client.get("/api/state").json
        followups = [row for row in state["followups"] if row["lead_id"] == lead_id]
        self.assertEqual(followups, [])

    def test_opt_out_cancels_followups(self):
        data = {"name": "Opt Out", "email": "optout@example.com", "budget": 8,
                "timeline": 30, "location": "Hyderabad", "property": "3 BHK", "consent": True}
        lead_id = self.client.post("/api/leads", json=data).json["id"]
        self.assertEqual(self.client.put(f"/api/leads/{lead_id}", json={"opted_out": True}).status_code, 200)
        state = self.client.get("/api/state").json
        statuses = [row["status"] for row in state["followups"] if row["lead_id"] == lead_id]
        self.assertTrue(statuses)
        self.assertTrue(all(status == "Cancelled" for status in statuses))

    def test_marketing_and_chat_offline_fallback(self):
        os.environ.pop("GEMINI_API_KEY", None)
        marketing = self.client.post("/api/marketing", json={"topic": "Kitchen"})
        self.assertEqual(marketing.status_code, 200)
        self.assertIn("template", marketing.json["result"]["mode"])
        chat = self.client.post("/api/chat", json={"question": "What services do you offer?"})
        self.assertEqual(chat.status_code, 200)
        self.assertIn("template", chat.json["mode"])

    def test_consultation_conflict(self):
        booking = {"name": "Appointment", "email": "appointment@example.com",
                   "starts_at": "2027-01-10T11:00:00"}
        self.assertEqual(self.client.post("/api/consultations", json=booking).status_code, 201)
        self.assertEqual(self.client.post("/api/consultations", json=booking).status_code, 409)

    def test_project_progress_and_overdue_monitor(self):
        project = self.client.post("/api/projects", json={
            "name": "Progress Test", "customer_name": "Synthetic Customer", "budget": 100
        })
        project_id = project.json["id"]
        milestone = self.client.post(f"/api/projects/{project_id}/milestones", json={
            "name": "Design approval", "due": "2020-01-01", "position": 1
        })
        milestone_id = milestone.json["id"]
        state_before = self.client.get("/api/state").json
        project_before = next(p for p in state_before["projects"] if p["id"] == project_id)
        self.assertEqual(project_before["progress"], 0)
        self.client.post(f"/api/milestones/{milestone_id}/complete", json={})
        project_after = next(p for p in self.client.get("/api/state").json["projects"] if p["id"] == project_id)
        self.assertEqual(project_after["progress"], 100)
        monitor = self.client.post("/api/monitor", json={})
        self.assertIn("alerts", monitor.json)

    def test_payment_alert(self):
        projects = self.client.get("/api/state").json["projects"]
        result = self.client.post("/api/payments", json={
            "project_id": projects[0]["id"], "label": "Final payment",
            "amount": 50000, "due": "2020-01-01", "status": "Pending"
        })
        self.assertEqual(result.status_code, 201)
        self.assertIn("overdue_payments", self.client.post("/api/monitor").json["alerts"])

    def test_dashboard_calculations(self):
        state = self.client.get("/api/state").json
        metrics = state["metrics"]
        self.assertEqual(metrics["total_leads"], len(state["leads"]))
        self.assertEqual(metrics["hot_leads"] + metrics["warm_leads"] + metrics["cold_leads"], len(state["leads"]))

    def test_automation_error_recording_is_available(self):
        state = self.client.get("/api/state").json
        self.assertIn("automation", state)

    def test_staff_routes_require_authentication(self):
        anonymous = app.test_client()
        self.assertEqual(anonymous.get("/api/state").status_code, 401)
        self.assertEqual(anonymous.get("/api/leads/export").status_code, 401)
        self.assertEqual(anonymous.post("/api/reset").status_code, 401)

    def test_n8n_header_authentication(self):
        os.environ["N8N_API_KEY"] = "test-n8n-key"
        anonymous = app.test_client()
        response = anonymous.post(
            "/api/monitor",
            headers={"X-InteriorFlow-Key": "test-n8n-key"},
        )
        self.assertEqual(response.status_code, 200)

    def test_malicious_source_is_normalized(self):
        data = {
            "name": "Source Test",
            "email": "source@example.com",
            "budget": 10,
            "timeline": 30,
            "location": "Hyderabad",
            "property": "2 BHK",
            "lead_source": "</span><img src=x onerror=alert(document.domain)>",
            "consent": False,
        }
        created = self.client.post("/api/leads", json=data)
        self.assertEqual(created.status_code, 201)
        lead = next(row for row in self.client.get("/api/state").json["leads"]
                    if row["email"] == "source@example.com")
        self.assertEqual(lead["source"], "Website")


if __name__ == "__main__":
    unittest.main()
