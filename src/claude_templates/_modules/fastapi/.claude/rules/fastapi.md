# FastAPI Best Practices

## Router Organization

- One router per domain/feature: `api/users.py`, `api/orders.py`
- Group related endpoints in the same router
- Use `prefix` and `tags` for organization:
  ```python
  router = APIRouter(prefix="/users", tags=["users"])
  ```
- Register routers in a central `api/__init__.py` or `main.py`

## Dependency Injection

Use `Depends()` for all shared resources:

```python
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

@router.get("/users/{user_id}")
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    ...
```

- Create reusable dependencies for: DB sessions, auth, pagination, config
- Dependencies can depend on other dependencies (composition)
- Use `Annotated` for cleaner type hints: `DB = Annotated[AsyncSession, Depends(get_db)]`

## Request/Response Models

- Always use Pydantic models for request bodies and responses
- Separate models: `UserCreate`, `UserUpdate`, `UserResponse`
- Use `response_model` parameter on endpoints for automatic serialization
- Never expose internal model (ORM) directly — always map to a response model

## Error Handling

- Services raise `ValueError` (client error) or `RuntimeError` (server error)
- API catches and maps to `HTTPException`:
  ```python
  try:
      result = await service.create_user(data)
  except ValueError as e:
      raise HTTPException(status_code=400, detail=str(e))
  except RuntimeError as e:
      raise HTTPException(status_code=500, detail="Internal error")
  ```
- Use exception handlers for global error formatting
- Never expose internal tracebacks to clients

## Async Endpoints

- Use `async def` for all endpoints that do I/O
- NEVER use synchronous blocking calls in async endpoints
- Use `BackgroundTasks` for fire-and-forget work
- Use `run_in_executor` for CPU-bound work that would block the event loop

## Lifespan Events

Use the lifespan context manager for startup/shutdown:

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create pools, warm caches
    yield
    # Shutdown: close pools, flush buffers
```

## Middleware

- CORS: configure explicitly, never use `allow_origins=["*"]` in production
- Request ID: add a unique ID to every request for tracing
- Keep middleware lightweight — runs on every request

## Anti-Patterns — NEVER Do

1. **Business logic in endpoints** — move to service layer
2. **Direct DB queries in endpoints** — use repository/service pattern
3. **Returning ORM objects directly** — map to Pydantic response models
4. **Synchronous DB calls in async endpoints** — blocks the event loop
5. **Wildcard CORS in production** — specify allowed origins
6. **No input validation** — always use Pydantic request models
