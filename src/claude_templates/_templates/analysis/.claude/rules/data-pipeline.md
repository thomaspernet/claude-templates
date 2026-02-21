---
paths:
  - "**/data-source/**"
  - "**/data-processing/**"
  - "**/src/**"
---

# Data Pipeline Rules

## Data Source

- Each download script must document: provider, API/URL, data description, update frequency
- Never modify raw data after initial download — treat `data-source/` outputs as immutable
- Store raw files in a clear structure (e.g., `data-source/{provider}/{date}/`)
- If using AWS: follow [`aws-python`](https://github.com/thomaspernet/aws-python) patterns for S3 uploads and Glue registration

## Data Processing

- Every processing notebook/script starts by documenting: input data, transformations, output dataset
- Use pandas or polars for transformations — prefer polars for datasets > 1M rows
- Processing must be idempotent — re-running produces identical results
- Create one notebook or script per logical transformation step
- Organize into subfolders by domain or pipeline stage
- Validate data shape and types after every major transformation
- Log row counts at each step — catch silent data loss

## pandas

- NEVER use `inplace=True` — always assign the result
- NEVER use chained indexing (`df[col][row]`) — use `.loc[]` or `.iloc[]`
- Always use `.copy()` when subsetting to avoid SettingWithCopyWarning
- Handle NaN explicitly — don't let missing values propagate silently
- Specify `dtype` parameter on `read_csv()` / `read_parquet()`
- Use `.pipe()` for readable transformation chains

## polars

- Use lazy evaluation (`.lazy()` → `.collect()`) for complex pipelines
- Prefer expressions over `.apply()` — expressions are vectorized and fast

## Schema Documentation

Every derived dataset must include a docstring or markdown cell explaining:

1. **Source data** — Which raw files or tables are used
2. **Joins** — What keys are used, inner/left/outer
3. **Filters** — What rows are excluded and why
4. **Aggregations** — What level of granularity, what metrics
5. **Business logic** — Any domain-specific rules applied

## Anti-Patterns — NEVER Do

1. **Undocumented transformations** — every step must explain what and why
2. **Hardcoded file paths** — use `pathlib.Path` relative to project root or config
3. **Processing without schema validation** — check column types and nullability
4. **Mixing download and processing** — keep `data-source/` and `data-processing/` separate
5. **Silent data loss** — always log row counts before and after transformations
