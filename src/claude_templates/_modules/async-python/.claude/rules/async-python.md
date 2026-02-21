# Async Python Best Practices

## Core Patterns

### asyncio.gather — Concurrent Independent Tasks

```python
results = await asyncio.gather(
    fetch_users(),
    fetch_orders(),
    fetch_products(),
)
```

Use when tasks are independent and you want all results.

### TaskGroup — Structured Concurrency (Python 3.11+)

```python
async with asyncio.TaskGroup() as tg:
    task1 = tg.create_task(fetch_users())
    task2 = tg.create_task(fetch_orders())
# All tasks complete or all cancel on first exception
```

Prefer over `gather` — better error handling, automatic cleanup.

### Semaphore — Rate Limiting

```python
sem = asyncio.Semaphore(10)  # max 10 concurrent

async def limited_fetch(url: str):
    async with sem:
        return await fetch(url)

results = await asyncio.gather(*[limited_fetch(u) for u in urls])
```

Use when calling external APIs with rate limits.

## Event Loop Rules

- NEVER call `asyncio.run()` inside an already-running loop
- NEVER use `time.sleep()` in async code — use `asyncio.sleep()`
- NEVER call synchronous blocking I/O in async functions — use `run_in_executor`:
  ```python
  result = await loop.run_in_executor(None, blocking_function)
  ```
- One event loop per thread. Don't create new loops in background threads.

## Async Generators

```python
async def stream_results(query: str):
    async for row in db.execute_stream(query):
        yield transform(row)

async for result in stream_results("SELECT ..."):
    process(result)
```

Use for processing large datasets without loading everything into memory.

## Common Pitfalls

### Missing await

```python
# Bug: returns coroutine object, doesn't execute
result = fetch_data()   # Missing await!

# Correct
result = await fetch_data()
```

Missing `await` is silent — the coroutine is created but never executed.

### Blocking the Event Loop

```python
# Bad: blocks entire event loop
data = requests.get(url)          # synchronous!
result = heavy_computation(data)  # CPU-bound!

# Good: use async HTTP client
data = await httpx.AsyncClient().get(url)
# Good: offload CPU work
result = await asyncio.to_thread(heavy_computation, data)
```

### Shared Mutable State

```python
# Bad: race condition
counter = 0
async def increment():
    global counter
    counter += 1  # Not atomic!

# Good: use asyncio.Lock
lock = asyncio.Lock()
async def safe_increment():
    async with lock:
        counter += 1
```

### Database Connections

- Each task/coroutine gets its own connection — NEVER share connections
- Use connection pools (asyncpg, SQLAlchemy async)
- Close connections in `finally` or use async context managers

## Testing Async Code

```python
import pytest

@pytest.mark.asyncio
async def test_fetch_users():
    result = await fetch_users()
    assert len(result) > 0
```

- Use `pytest-asyncio` with `@pytest.mark.asyncio`
- Mock async functions with `AsyncMock`:
  ```python
  from unittest.mock import AsyncMock
  mock_db = AsyncMock(return_value=[{"id": 1}])
  ```

## Anti-Patterns — NEVER Do

1. **Missing await** — silent bug, coroutine never executes
2. **time.sleep() in async code** — blocks the entire event loop
3. **requests library in async code** — use httpx or aiohttp
4. **Sharing DB connections between tasks** — race conditions, corrupted state
5. **asyncio.run() inside running loop** — RuntimeError
6. **Ignoring exceptions in gather** — use `return_exceptions=True` or TaskGroup
