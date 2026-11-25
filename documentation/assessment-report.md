# AI-Powered Marketing and Business Process Automation for Sha Interface Interiors

**Prepared by:** Charan Thota  
**Position:** AI Marketing & Automation Intern

## Executive summary
This independent assessment prototype demonstrates a locally reproducible automation strategy for enquiry capture, lead qualification, follow-ups, marketing drafts, consultations, project monitoring and payment alerts. It uses Flask, SQLite, optional Gemini and n8n. It does not contact live customers or publish content externally.

## Company and customer journey
Public research indicates a Hyderabad interior design business established in 2012 offering turnkey residential and commercial interiors, modular furniture and 3D visualization. The prototype supports a journey from public enquiry to qualification, consultation, project lifecycle and feedback.

## Prioritized opportunity
1. Immediate central lead capture
2. Explainable qualification
3. Consent-based follow-up
4. Human-approved marketing
5. Consultation conflict control
6. Project and payment deadline monitoring
7. Feedback escalation

## Solution and architecture
The browser calls a Flask REST API backed by SQLite. Optional Gemini calls remain server-side. n8n imports webhook and scheduled workflows and calls the same APIs. The prototype includes offline template responses.

## Security and privacy
Synthetic data, server-side secrets, parameterized SQL, consent flags, opt-out cancellation and no external sending are implemented. Authentication, webhook signatures, role authorization and production encryption remain required.

## Testing
The automated unittest suite reports 14 passing tests covering lead, consent, scoring, fallback AI, appointments, project progress, payments and dashboard metrics.

## Limitations
Company policies, exact pricing, warranty terms and internal conversion baselines require owner confirmation. Gemini, Gmail, Google Calendar and WhatsApp credentials were not provided. The prototype was not deployed or connected to the live company website.

## Roadmap
Pilot in a staging environment, measure baseline response and conversion, confirm scoring and policies, integrate approved provider credentials, migrate to PostgreSQL and then expand RAG and project APIs.
