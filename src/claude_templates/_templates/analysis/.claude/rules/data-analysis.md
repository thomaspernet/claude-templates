---
paths:
  - "**/*.py"
  - "**/src/**"
---

# Data Analysis Rules

## pandas

- NEVER use `inplace=True` — always assign the result
- NEVER use chained indexing (`df[col][row]`) — use `.loc[]` or `.iloc[]`
- Always use `.copy()` when subsetting to avoid SettingWithCopyWarning
- Handle NaN explicitly — don't let missing values propagate silently
- Specify `dtype` parameter on `read_csv()` / `read_parquet()` — prevent silent coercion
- Use `.pipe()` for readable transformation chains
- Prefer `.assign()` over direct column assignment for chaining

## polars

- Prefer polars over pandas for datasets > 1M rows
- Use lazy evaluation (`.lazy()` → `.collect()`) for complex pipelines
- Prefer expressions over `.apply()` — expressions are vectorized and fast

## General

- Pin random seeds for any stochastic operation
- Document data assumptions with inline comments
- Validate data shape and types after every major transformation
- Log row counts at each pipeline step — catch silent data loss
- Use `assert` statements for data invariants during development
- Store intermediate results in `data/processed/` — not in memory only
