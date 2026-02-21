---
paths:
  - "**/backend/**"
  - "**/api/**"
  - "**/services/**"
  - "**/infrastructure/**"
---

# Backend Rules — DDD Architecture

## Layer Responsibilities

| Layer | MUST do | MUST NOT do |
|-------|---------|-------------|
| API | Parse requests, return responses, catch exceptions → HTTPException | Contain business logic, run DB queries |
| Service | Orchestrate business logic, validate rules, raise ValueError/RuntimeError | Import from API, access DB directly |
| Domain | Define entities, value objects, enums | Import from any other layer |
| Infrastructure | Implement repository interfaces, run DB queries, call external APIs | Contain business logic |

## Patterns

- **Repository pattern**: Abstract interface in domain/, concrete implementation in infrastructure/
- **Dependency injection**: Services receive repositories via constructor or FastAPI Depends()
- **Pydantic models**: `Entity`, `EntityCreate`, `EntityUpdate`, `EntityResponse`
- **Error flow**: Service raises `ValueError` (client error) or `RuntimeError` (server error) → API catches → `HTTPException(400)` or `HTTPException(500)`

## Async Rules

- ALL database operations MUST be async
- ALL async functions MUST be awaited — missing awaits cause silent failures
- Use `async for` for streaming results
- Each request/task gets its own DB connection — never share connections

## Common Violations

- DB query in an API endpoint → Move to infrastructure/ repository
- Business logic in API route → Move to service layer
- Missing `await` on async call → Add await, test for correctness
- Shared DB connection between tasks → Each task gets own connector
