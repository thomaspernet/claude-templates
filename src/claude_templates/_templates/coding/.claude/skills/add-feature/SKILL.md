---
name: add-feature
description: "Step-by-step DDD feature implementation. Use when adding a new entity, endpoint, or business capability."
---

# Add Feature — DDD Implementation

Follow these steps in order. Do NOT skip layers.

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

## Checklist

- [ ] Domain models created with type hints
- [ ] Repository interface defined
- [ ] Infrastructure implementation with DB queries
- [ ] Service with business logic
- [ ] API endpoints with error handling
- [ ] Tests written and passing
