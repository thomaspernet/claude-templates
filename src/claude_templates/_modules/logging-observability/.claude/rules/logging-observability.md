# Logging & Observability Best Practices

## Structured Logging

Always log as structured data (JSON), not plain strings:

```python
# Good: structured, parseable
logger.info("user_created", extra={"user_id": user.id, "email": user.email})

# Bad: unstructured, hard to parse
logger.info(f"Created user {user.id} with email {user.email}")
```

Use a structured logger (structlog, python-json-logger) for automatic JSON output.

## Log Levels

| Level | When | Example |
|-------|------|---------|
| DEBUG | Development details | Variable values, query text |
| INFO | Normal operations | Request handled, job completed |
| WARNING | Unexpected but handled | Retry attempt, fallback used |
| ERROR | Failed operation | Unhandled exception, API failure |
| CRITICAL | System-level failure | Database unreachable, out of memory |

- Default to INFO in production
- Enable DEBUG only for specific modules when investigating
- ERROR should always include the full exception traceback

## Correlation IDs

Tag every log entry with a request/trace ID:

```python
import uuid

request_id = str(uuid.uuid4())[:8]
logger.info("processing_request", extra={"request_id": request_id})
```

- Generate at the entry point (API middleware, queue consumer)
- Pass through all function calls
- Include in error responses to users for support debugging
- Prefix format: `[abc12345]` for easy grep

## What to Log

### Always Log

- Request received (method, path, user ID)
- Request completed (status code, duration)
- External API calls (URL, status, duration)
- Background job start/end (job name, duration, result)
- Errors with full context (traceback, input data)

### Never Log

- Passwords, tokens, API keys
- Full credit card numbers
- Personal data beyond what's needed (SSN, medical records)
- Request/response bodies in production (too verbose, PII risk)

## Tracing

For distributed systems:
- Use OpenTelemetry for cross-service tracing
- Propagate trace context in HTTP headers
- Instrument: HTTP clients, database calls, queue operations
- Set span attributes for key business data

## Metrics

| Type | Use | Example |
|------|-----|---------|
| Counter | Events that only increase | Requests served, errors |
| Histogram | Value distributions | Response time, payload size |
| Gauge | Current state | Active connections, queue depth |

Key metrics to track:
- Request rate, error rate, duration (RED method)
- Saturation: CPU, memory, disk, connections

## Alerting Rules

- Alert on symptoms, not causes: "error rate > 5%" not "CPU > 80%"
- Set thresholds based on SLOs, not arbitrary numbers
- Include runbook links in alert descriptions
- Avoid alert fatigue — only alert on actionable conditions

## Anti-Patterns — NEVER Do

1. **Logging PII** — passwords, tokens, personal data
2. **Swallowing exceptions** — `except: pass` hides failures
3. **Log-and-throw** — don't log an error then re-raise (logs duplicate)
4. **No request IDs** — impossible to trace issues across logs
5. **Logging at wrong level** — expected 404s are not ERRORs
6. **Unstructured logs in production** — can't search, can't alert
