# AI marketing and automation — Sha Interface Interiors
Prepared for the AI Marketing & Automation Intern assessment | Charan Thota

## Executive summary
Prioritize enquiry capture, qualification, follow-up and marketing drafts. A local prototype demonstrates how a lead becomes a scored record and a consent-based task. A deadline monitor identifies overdue work. Optional Gemini integration drafts marketing content and answers questions using limited demo context.

## Company and industry research
Research starting points: https://sha-interiors-hyderabad.com/ and https://www.houzz.com/research . Company website features and industry statistics require independent verification before submission. The following are operational hypotheses, not confirmed internal problems or survey results.

| Bottleneck | Automation | Measurement |
|---|---|---|
| Missed enquiries | Webhook to central lead database | captured enquiries / received enquiries |
| Manual qualification | Explainable budget and readiness score | minutes per lead |
| Missed follow-ups | Consent-based scheduled tasks | completed / due tasks |
| Repetitive marketing | AI drafts with human approval | minutes per approved post |
| Repeated questions | Grounded assistant and escalation | response time and accuracy |
| Design revisions | Versioned approvals (future) | revision cycles |
| Procurement delays | Milestone monitoring | overdue tasks |
| Payment delays | Due-date reminders (future) | days outstanding |

## Implementation
Browser -> Flask API -> SQLite. Lead submission validates input, rejects duplicate email, scores budget (15/35/50), timeline (10/25/40) and location (0/10), saves a draft and creates a task only with consent. These thresholds are assumptions, not company policy. Marketing and chat call Gemini when configured; otherwise templates are explicitly labeled. n8n can invoke the deadline monitor daily. No customer messages are sent.

## Pilot and ROI
Illustrative assumptions: 100 leads/month, 5 minutes saved each = 8.3 hours; 20 marketing drafts/month, 15 minutes saved each = 5 hours. Total 13.3 hours/month before review overhead. At INR 300/hour this is INR 3,990 gross labor value, not measured savings. Subtract hosting, API and maintenance costs. Compare baseline and pilot response time, conversion, follow-up coverage and accuracy.

## Rollout
Week 1: validate existing CRM and consent process. Week 2: integrate enquiry webhook in staging. Week 3: pilot follow-ups and marketing approvals. Week 4: measure outcomes and improve scoring. Later: calendar, WhatsApp, procurement, payments and feedback integrations.

## Risks
Use synthetic data, no real outbound communication, no binding quotes, human review for AI content, restricted credentials, authentication before deployment, and monitoring for duplicate or failed events. Internal systems and policies are unknown. This is a local MVP, not a production solution.

## Demo script
Show lead form, score and task; repeat to show duplicate rejection; generate a marketing draft; ask a customer question; run deadline monitor and complete a task; explain template versus live AI modes and show n8n execution after local setup.
