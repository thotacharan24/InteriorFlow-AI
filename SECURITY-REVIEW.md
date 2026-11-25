# InteriorFlow AI - Security Review Summary

Review date: 2026-11-25

| # | Severity | File | Lines | Vulnerability | Confidence |
|---|----------|------|-------|---------------|------------|
| 1 | 🟠 HIGH | app.py | Staff-sensitive routes | Missing authentication and authorization | 10/10 |
| 2 | 🟠 HIGH | index.html; app.py | Source chart and lead source handling | Stored DOM string injection and unbounded source value | 10/10 |

## Remediation
1. Added staff session authentication and protected staff state, export, mutation and reset routes.
2. Added n8n shared-header authentication for automation endpoints.
3. Added server-side lead-source allowlisting.
4. Added HTML escaping before chart source labels are rendered.
5. Added baseline security headers including CSP, nosniff, frame denial and referrer policy.

## Remaining security blockers
- Replace demo credentials with production identity and password controls.
- Rotate the Flask secret and n8n key through environment variables.
- Add CSRF protection, password hashing, session hardening, rate limiting and authorization roles.
- Add HTTPS and production database controls before deployment.
