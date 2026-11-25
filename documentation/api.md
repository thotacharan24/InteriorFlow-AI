# API Reference

## Lead capture
`POST /api/leads`

Example: `{"name":"Demo Customer","email":"demo@example.com","budget":12,"timeline":30,"location":"Hyderabad","property":"3 BHK","consent":true}`

Success: `201 {"id":31,"score":100,"classification":"Hot","package":"...","draft":"..."}`

## Marketing
`POST /api/marketing`

Example: `{"topic":"Modern modular kitchen","platform":"Instagram","audience":"Hyderabad homeowners","objective":"Generate qualified enquiries","tone":"Warm and premium"}`

## Chat
`POST /api/chat` with `{"question":"What services are offered?"}`

## Consultation
`POST /api/consultations` with `{"name":"Demo","email":"demo@example.com","starts_at":"2027-01-10T11:00:00"}`

## State
`GET /api/state` returns all demonstration records and calculated dashboard metrics.

## Monitoring
`POST /api/monitor` identifies overdue tasks, milestones, payments and expired campaigns.
