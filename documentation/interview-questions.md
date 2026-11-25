# Interview Preparation - 30 Questions

1. **What problem does it solve?** Capturing, qualifying and following up enquiries consistently.
2. **What is the architecture?** Browser UI to Flask REST endpoints and SQLite.
3. **Why Flask?** It is lightweight and suitable for a local, reproducible MVP.
4. **Why n8n?** It provides visual webhooks and schedules without custom infrastructure.
5. **Why Gemini?** It generates marketing drafts and can enhance customer responses.
6. **How does scoring work?** Budget, timeline, location, completeness and engagement contribute to 0-100.
7. **What are the thresholds?** 80+ Hot, 50-79 Warm, below 50 Cold. These are demo assumptions.
8. **How are duplicates prevented?** Email is unique in the database and SQLite enforces uniqueness.
9. **How is consent enforced?** Follow-ups are only scheduled when the lead consent flag is true.
10. **How is opt-out handled?** Updating a lead as opted out cancels pending follow-ups.
11. **How does offline chat work?** It uses verified public baseline knowledge and a template fallback.
12. **What is RAG in this project?** The prototype has a knowledge table and grounded prompt context but is not an embedding-based RAG system.
13. **How are API keys protected?** Gemini credentials remain in server-side environment variables.
14. **How is SQL injection prevented?** Queries use SQLite parameter binding.
15. **How are appointments de-duplicated?** Exact start times with scheduled status are checked.
16. **How is project progress calculated?** Completed milestones divided by total milestones.
17. **How are overdue items found?** Due dates before today's local date and incomplete status.
18. **How are AI outputs validated?** The app catches failures and returns explicitly labeled template content.
19. **Are messages sent automatically?** No. The prototype creates drafts only.
20. **What is a real workflow execution?** A call recorded in automation_logs from a successfully executed Flask endpoint.
21. **How would Gmail be integrated?** Only through approved credentials and test recipients.
22. **How would Google Calendar work?** OAuth credentials and conflict-aware calendar APIs are required.
23. **Why does the app label estimates?** Package prices and internal policies were not independently verified.
24. **How would the database scale?** Migration to PostgreSQL and managed indexes/backups would be next.
25. **How is deployment handled?** Docker is provided; no public deployment was performed.
26. **How is testing performed?** Python unittest covers the main API and business rules.
27. **What is the biggest limitation?** No production authentication or real provider credentials.
28. **What was measured?** 14 actual passing tests and local API behavior.
29. **How did you use AI tools?** To accelerate implementation and drafting while independently verifying code and claims.
30. **What would the next pilot measure?** Response time, follow-up coverage, lead conversion and staff review time.
