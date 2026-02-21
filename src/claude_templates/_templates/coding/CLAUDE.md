# {PROJECT_NAME}

## BUGS.md and MISTAKES.md — READ AND UPDATE (MANDATORY)

You MUST follow these rules every session. No exceptions.

1. **START OF SESSION**: Read `BUGS.md` and `MISTAKES.md` before making any changes.
2. **WHEN YOU HIT A BUG**: Add entry to `BUGS.md` BEFORE attempting the fix.
3. **WHEN YOU MAKE A MISTAKE**: Add entry to `MISTAKES.md` BEFORE fixing it.
4. **WHEN YOU FIX A BUG**: Update the entry status to FIXED with root cause.
5. **WHEN YOU COMMIT**: Include tracking files if modified.

## Project & Tech

- **Backend**: Python (FastAPI), managed with `uv`
- **Frontend**: TypeScript (Next.js / React), managed with `npm`
- **Database**: {DATABASE}
- **Key directories**: `backend/`, `frontend/`, `tests/`, `docs/`

## Architecture — Domain-Driven Design (4 Layers)

```
API/Presentation  →  Application/Service  →  Domain  →  Infrastructure
     (HTTP)           (orchestration)       (models)    (DB, external)
```

Dependencies flow **inward only**. Never import from an outer layer.

| Layer | Responsibility | Contains |
|-------|---------------|----------|
| API | HTTP handling, request/response | Routers, middleware, DTOs |
| Service | Business logic orchestration | Use cases, workflows |
| Domain | Core models and rules | Entities, value objects, enums |
| Infrastructure | External system access | Repositories, API clients, DB queries |

## Critical Rules

1. **No business logic in API endpoints** — API catches exceptions and returns HTTP responses. Logic lives in services.
2. **No DB queries outside infrastructure** — All Cypher/SQL lives in repository implementations.
3. **All async operations MUST be awaited** — Missing awaits cause silent failures.
4. **Type hints on every function** — Parameters and return types. No exceptions.
5. **No magic strings** — Use constants or enums.
6. **Services raise ValueError/RuntimeError** — API layer catches and maps to HTTPException (400/500).
7. **Pydantic model naming**: `Entity`, `EntityCreate`, `EntityUpdate`, `EntityResponse`.
8. **No code in `__init__.py`** — Exports only.

## Code Style

- Python: `snake_case` functions/variables, `PascalCase` classes
- TypeScript: `camelCase` functions/variables, `PascalCase` components
- Early returns to avoid deep nesting
- Fix root causes, not symptoms
- Start simple, add complexity only when needed

## Dev Commands

```bash
# Backend
uv run pytest                    # Run tests
uv run pytest --cov             # Tests with coverage
uv run ruff check backend/      # Lint
uv run uvicorn main:app --reload # Run dev server

# Frontend
npm run dev                      # Dev server
npm run build                    # Production build
npm run lint                     # Lint
npm test                         # Tests
```

## Testing

- **Framework**: pytest + pytest-asyncio
- **Coverage target**: 80%+
- **Mock all external calls** — DB, APIs, file system
- **Test naming**: `test_{function}_{scenario}_{expected}`
- Frontend: Run `npm run build` — must pass with zero errors

## Development Workflow

- Commit prefixes: `fix:`, `feat:`, `refactor:`, `docs:`, `chore:`, `test:`
- NEVER force push without asking first
- NEVER commit secrets or credentials
- Start complex changes in Plan Mode (Shift+Tab x2)
- When compacting context, preserve: modified files, test results, current bugs, failed approaches
