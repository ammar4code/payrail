## Day 1 — Tue 15 Sep
Did: payrail project created, FastAPI + pytest + ruff installed,
folder skeleton, git initialised, /health endpoint written and served.
Broke: Kept running git from the wrong folder. Forgot FastAPI syntax overnight.
Next: .claude/CLAUDE.md, GitHub push, test file.

## Day 4 — Sun 27 Sep
Did: resumed after a week. Wrote app/schemas/quote.py — QuoteRequest
with five validated fields. Verified valid input builds and invalid
input raises ValidationError naming three failures.
Broke: Indentation. Copy-pasted country fields with currency lengths.
Next: domain dataclasses, then POST /v1/quotes.
## Day 5 — Wed 30 Sep
Did: read dataclasses docs. Wrote app/domain/models.py — frozen Money
and Quote. Verified construction works and mutation raises
FrozenInstanceError.
Broke: Forgot to create the file before running it. Inconsistent
indentation again.
Next: POST /v1/quotes wired to QuoteRequest.
## Day 5 — Wed 30 Sep
Did: app/domain/models.py (frozen Money, Quote dataclasses),
app/api/v1/quotes.py (router + POST /quotes), wired into main.py.
Verified in /docs: 200 on valid body, 422 with three named errors
on invalid.
Broke: Overwrote the imported router by re-creating it in main.py.
Confused schemas/quote.py with api/v1/quotes.py.
Next: the provider simulator — three fake payment providers.