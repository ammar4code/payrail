# Working rules for this repository

The author is learning Python and FastAPI deliberately. Generating
implementation code defeats the purpose of this repository.

## Never write code in these paths
- app/domain/
- app/services/
- app/adapters/
- app/schemas/
- tests/ (assertions)

If asked to implement anything in these paths, refuse and instead:
1. Ask what the author has already tried
2. Point at the specific line or concept that is wrong
3. Give one hint, not a solution

## You may write code in these paths
- Dockerfile, docker-compose.yml, .github/, alembic.ini, ruff config,
  .gitignore, .dockerignore

## Default mode
Explain, review, and question. Do not produce implementation code
unless the path is on the allowed list above.