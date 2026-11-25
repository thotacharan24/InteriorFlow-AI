from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "final-submission"
OUT.mkdir(exist_ok=True)

title = "AI-Powered Marketing and Business Process Automation for Sha Interface Interiors"
prepared = "Prepared by: Charan Thota\nPosition: AI Marketing & Automation Intern"

sections = [
    ("Cover", title + "\n" + prepared),
    ("Executive summary", "This independent assessment prototype demonstrates enquiry capture, qualification, consent-based follow-ups, marketing drafts, consultations, project monitoring, payments and n8n automation. It uses Flask, SQLite, optional Gemini and local synthetic data."),
    ("Company overview", "Public website research indicates a Hyderabad interior design company established in 2012. It offers turnkey projects, bespoke modular furniture, modular kitchens, colour coordination and 3D visualization."),
    ("Industry and competitor research", "Key bottlenecks are missed enquiries, slow qualification, inconsistent follow-up, revision churn, vendor coordination and fragmented communication. Public competitor models emphasize digital consultation, package discovery and project tracking."),
    ("Proposed solution", "A browser dashboard submits enquiries to Flask REST APIs. SQLite stores customers and operational records. Gemini is optional and server-side. n8n workflows call webhooks or HTTP endpoints."),
    ("MVP implementation", "Implemented: 30 synthetic leads, explainable lead scoring, Hot/Warm/Cold classification, consent and opt-out, marketing drafts, consultation conflict checks, project milestones, overdue monitoring and dashboard metrics."),
    ("Testing", "Actual result: 17 unittest cases passed, 0 failed on 2026-11-25. Browser desktop and mobile layouts were captured locally. n8n and live Gemini execution were not claimed."),
    ("Security", "Synthetic data, server-side API keys, parameterized SQL, consent fields, opt-out handling and human-approved drafts are implemented. Authentication, provider OAuth and production authorization remain required."),
    ("Limitations", "Company policies, exact pricing, warranties and internal baselines require staff confirmation. Gemini, Gmail, Google Calendar and WhatsApp credentials were not provided."),
    ("Roadmap", "Pilot with measured baselines, confirm policies, integrate approved providers, migrate to PostgreSQL and expand retrieval-augmented knowledge."),
]

doc = Document()
doc.core_properties.title = title
doc.core_properties.author = "Charan Thota"

heading = doc.add_heading(title, level=1)
heading.alignment = WD_ALIGN_PARAGRAPH.CENTER
p = doc.add_paragraph(prepared)
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_page_break()

for name, body in sections:
    if name != "Cover":
        doc.add_heading(name, level=1)
        doc.add_paragraph(body)

doc.save(OUT / "assessment-report.docx")

pdf = SimpleDocTemplate(str(OUT / "assessment-report.pdf"), pagesize=A4,
                        rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
styles = getSampleStyleSheet()
story = [Paragraph(title, styles["Title"]), Spacer(1, 12),
         Paragraph(prepared.replace("\n", "<br/>"), styles["Normal"]), Spacer(1, 24)]
for name, body in sections:
    if name == "Cover":
        continue
    story.append(Paragraph(name, styles["Heading1"]))
    story.append(Paragraph(body, styles["BodyText"]))
    story.append(Spacer(1, 10))
pdf.build(story)

print("Created assessment-report.docx and assessment-report.pdf")
