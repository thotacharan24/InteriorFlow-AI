# Test Report

Test command: `py -m unittest discover -s tests -v`

## Actual result
- 17 tests executed
- 17 passed
- 0 failed
- Test date: 2026-11-25

## Covered behaviors
Lead creation, duplicate detection, invalid fields, scoring boundaries, package labels, consent, opt-out, offline marketing/chat fallback, appointment conflicts, project progress, payment alert monitoring and dashboard calculation.

## Known warnings
Python emitted ResourceWarning and datetime deprecation warnings during portions of the suite. These do not indicate a failing test but should be cleaned during production hardening.

## Browser verification
Desktop and mobile screenshots were captured with Playwright from the running local application:
- `dashboard-desktop.png`
- `dashboard-mobile.png`
