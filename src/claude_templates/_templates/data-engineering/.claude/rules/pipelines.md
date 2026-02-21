---
paths:
  - "**/pipelines/**"
  - "**/flows/**"
  - "**/tasks/**"
---

# Pipeline Rules

## Idempotency

- Every pipeline MUST be safely re-runnable
- Use UPSERT (INSERT ON CONFLICT UPDATE), not INSERT
- Use MERGE for Neo4j, not CREATE
- Track last-run timestamps for incremental loads

## Error Handling

- Catch specific exceptions, not bare `except:`
- Log the full traceback, then re-raise or handle
- Use retry with exponential backoff for transient failures (network, rate limits)
- Set max retries (3) — don't retry forever

## Logging

MUST log at each step:
```
INFO  | Pipeline {name} started
INFO  | Extract: {n} rows from {source}
INFO  | Transform: {n} rows → {m} rows (filtered {n-m})
INFO  | Load: {m} rows written to {target}
INFO  | Pipeline {name} completed in {duration}s
ERROR | Pipeline {name} failed at step {step}: {error}
```

## Task Isolation

- Each Prefect task gets its own DB connector — NEVER pass connections between tasks
- Tasks should be pure functions: input → output
- Side effects (DB writes) happen at task boundaries
- Use `.submit()` for parallel task execution

## Data Validation

- Validate schema BEFORE processing (column names, types, non-null constraints)
- Validate output BEFORE writing (row counts, value ranges, uniqueness)
- Fail fast on validation errors — don't write bad data
