---
name: add-feature
description: "Use this skill when adding a new entity, endpoint, or business capability. Invoke when the user describes a new feature that needs domain models, a service layer, API routes, or database access — even if they haven't thought through all four layers yet."
---

# Add Feature — DDD Implementation

## When to Use

**Perfect for:**
- Adding a new entity with full CRUD
- Adding a new API endpoint backed by business logic
- Adding a new business capability that spans multiple layers

**Not ideal for:**
- Modifying an existing entity (edit only the affected layers)
- Schema-only changes or migrations
- Frontend-only features with no backend changes

---

> **Core Philosophy:** Build the correct layer contract first, then implement upward. A feature exists when all four layers are in place and tested — not before.

## ⚠️ CRITICAL

1. **Never import across layers in the wrong direction.** API → Service → Domain → Infrastructure only. Domain MUST NOT import from Service or Infrastructure. Service MUST NOT import from API.
2. **All DB queries live in Infrastructure.** A Cypher or SQL statement anywhere else is an architecture violation. No exceptions.
3. **Do NOT skip layers.** Never call a repository directly from an API endpoint. Never put business logic in Infrastructure.

---

## Step 1: Domain Model

Create Pydantic models in `domain/`:
- `Entity` — core model with all fields
- `EntityCreate` — fields required for creation (no id, no timestamps)
- `EntityUpdate` — optional fields for partial update
- `EntityResponse` — what the API returns

## Step 2: Repository Interface

Create abstract repository in `domain/repositories/`:
- Define abstract methods: `create()`, `get_by_id()`, `list()`, `update()`, `delete()`
- Use the domain models as parameter and return types

## Step 3: Infrastructure Implementation

Implement the repository in `infrastructure/repositories/`:
- Concrete class inheriting from the abstract interface
- ALL database queries live here
- `_map_to_entity()` helper to convert DB records to domain models

## Step 4: Service Layer

Create service in `services/`:
- Receives repository via dependency injection
- Contains business logic and validation
- Raises `ValueError` for client errors, `RuntimeError` for server errors

## Step 5: API Endpoint

Create router in `api/`:
- FastAPI router with REST endpoints
- Dependency injection for service
- Catch `ValueError` → 400, `RuntimeError` → 500

## Step 6: Tests

- Unit tests for service logic (mock repository)
- Integration tests for API endpoints (mock service or use test DB)
- Verify all CRUD operations work end-to-end

## Output

Report the created files grouped by layer:

```
Domain:         domain/models/entity.py
                domain/repositories/entity_repo.py
Infrastructure: infrastructure/repositories/entity_repo_impl.py
Service:        services/entity_service.py
API:            api/routers/entity.py
Tests:          tests/unit/test_entity_service.py
                tests/integration/test_entity_api.py
```

## Checklist

- [ ] Domain models created with type hints
- [ ] Repository interface defined in Domain (no DB imports)
- [ ] Infrastructure implementation with all DB queries isolated
- [ ] Service with business logic, raises ValueError/RuntimeError
- [ ] API endpoints with correct error mapping (400/500)
- [ ] No cross-layer import violations
- [ ] Tests written and passing
