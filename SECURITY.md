# Security Notes

This repository is a local assessment prototype. It uses synthetic customer data and does not send real email or WhatsApp messages.

## Controls implemented
- Environment variables for database and Gemini configuration
- Server-side input validation
- Parameterized SQLite queries
- Explicit communication-consent fields
- Opt-out support for scheduled follow-ups
- Gemini key kept on the backend only
- Offline fallback that does not require credentials
- Human approval for generated marketing and communication drafts

## Before production
Add authenticated users and authorization, CSRF protection, secure webhook signatures, CORS restrictions, rate limiting, encrypted backups, audit retention, data deletion workflows and HTTPS. Replace SQLite with a managed database when concurrent users are expected.

Never commit `.env`, `demo.db`, API keys or real customer exports.
