# InteriorFlow AI
Independent assessment MVP for Sha Interface Interiors. Local synthetic data only.

## Project overview
InteriorFlow AI demonstrates lead qualification, consent-based follow-ups, Gemini-ready marketing drafts, a grounded offline chatbot, consultation booking, project monitoring, payment alerts and n8n webhook workflows.

## Features
- Responsive premium dashboard with 30 synthetic leads
- Lead scoring, classification, package recommendations and CSV export
- Lead edit/delete/search/filter/sort APIs
- Follow-up sequences, opt-out handling and consent enforcement
- Optional Gemini live mode and explicit template fallback
- Marketing draft saving, approval and internal scheduling
- Consultation conflict detection
- Project lifecycle, milestones and progress calculation
- Overdue task/payment/campaign monitoring
- Feedback sentiment recording and escalation
- Eight importable n8n workflow JSON files

## Windows VS Code setup
Open this folder in VS Code, then open Terminal > New Terminal (PowerShell).

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
.\.venv\Scripts\python.exe app.py
```
Open http://127.0.0.1:5000. No API key is needed for template mode. For live AI, obtain a Gemini API key from https://aistudio.google.com/apikey and put it in `.env`, then restart. Never commit that file.

Demo: submit Demo Customer, demo@example.com, budget 12, timeline 30, Hyderabad, 3 BHK, consent checked. Observe score 100, draft and follow-up task. Repeat to test duplicate prevention. Generate marketing content, ask a question, run deadline monitor and complete the overdue task.

Tests: `.\.venv\Scripts\python.exe -m unittest discover -s tests -v`

## n8n
Install Node.js and run `npx n8n` in a second terminal. Open http://localhost:5678 and import automation/monitor.json. Execute manually while Flask is running. Activate the schedule only after verifying it. If n8n is in Docker, change the URL to host.docker.internal:5000 and configure networking appropriately.

## Render deployment

The repository includes `render.yaml` for Render's free web-service tier.

Use Gunicorn:

```text
gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120
```

Configure these Render environment variables:

- `DEMO_SECRET_KEY`: strong random value
- `DEMO_USERNAME`: staff login username
- `DEMO_PASSWORD`: staff login password
- `N8N_API_KEY`: shared automation request key
- `GEMINI_API_KEY`: optional Gemini key
- `GEMINI_MODEL`: `gemini-2.5-flash`
- `DB_PATH`: `/tmp/interiorflow.db`

The free tier has ephemeral filesystem storage. Database contents may reset during deploy or restart.

## Scope
Flask + SQLite + plain HTML chosen for easy local setup. Lead capture, scoring, consent-based task creation, template drafts, optional Gemini marketing/chat, consultation, project monitoring, payment alerts and activity logs are implemented. No real messages are sent. Authentication, production deployment, full RAG and real Calendar/WhatsApp/Gmail integrations require credentials and authorization. Do not expose this local demo publicly. Delete demo.db with the server stopped to reset data. See `research/` and `documentation/` for the assessment materials.
