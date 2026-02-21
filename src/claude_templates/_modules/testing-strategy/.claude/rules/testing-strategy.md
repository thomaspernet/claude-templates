# Testing Strategy Best Practices

## Test Pyramid

```
        /  E2E  \        Few, slow, expensive
       / Integr. \       Some, medium speed
      /   Unit    \      Many, fast, cheap
```

- **Unit tests** (70%): Single functions, fast, no I/O
- **Integration tests** (20%): Multiple components together, may use test DB
- **E2E tests** (10%): Full user flows, browser/API level

## Unit Tests

- Test one behavior per test
- No I/O (no DB, no filesystem, no network)
- Fast: entire unit suite should run in seconds
- Use fixtures for shared setup

### Test Naming

```python
def test_{function}_{scenario}_{expected}():
    ...

# Examples:
def test_calculate_total_empty_cart_returns_zero():
def test_validate_email_missing_at_raises_value_error():
```

## Mocking Strategy

### When to Mock

- External APIs and services
- Database calls (in unit tests)
- Time-dependent functions (`datetime.now()`)
- Random/non-deterministic functions

### When NOT to Mock

- Your own pure functions — test them directly
- Data structures and models
- Simple utilities

### Mocking Rules

- Mock at the boundary, not deep inside
- Prefer dependency injection over patching
- Assert mock was called with expected arguments
- `AsyncMock` for async functions

## Fixture Patterns

```python
@pytest.fixture
def user():
    return User(name="Test User", email="test@example.com")

@pytest.fixture
def db_session():
    """Create a test database session."""
    session = create_test_session()
    yield session
    session.rollback()
    session.close()
```

- Use `yield` fixtures for setup/teardown
- Use `tmp_path` for file system tests
- Use `monkeypatch` for environment variables
- Keep fixtures focused — one concern per fixture

## Coverage

- Target: 80%+ for business logic
- Don't chase 100% — diminishing returns
- Measure branch coverage, not just line coverage
- Ignore: config files, `__init__.py`, type stubs

## TDD Workflow

1. **Red**: Write a failing test for the desired behavior
2. **Green**: Write the minimum code to make it pass
3. **Refactor**: Clean up while keeping tests green

Use TDD for complex logic. Skip for simple CRUD or wiring code.

## Anti-Patterns — NEVER Do

1. **Testing implementation, not behavior** — test WHAT it does, not HOW
2. **Brittle tests** — tests that break when you refactor (not change behavior)
3. **Testing framework internals** — trust SQLAlchemy, FastAPI, etc.
4. **No assertions** — a test without assertions is not a test
5. **Test interdependency** — each test must be independent and order-agnostic
6. **Mocking everything** — over-mocking makes tests pass regardless of correctness
7. **Slow test suites** — if tests take minutes, developers skip them
