---
paths:
  - "**/data-source/**"
  - "**/data-processing/**"
---

# Data Pipeline Rules

## Data Source

- Follow [`aws-python`](https://github.com/thomaspernet/aws-python) patterns for S3 uploads and Glue catalog registration
- Each download script must document: provider, API/URL, data description, update frequency
- Save raw data to S3 with clear partitioning (e.g., `s3://bucket/raw/{source}/{date}/`)
- Register all tables in the Glue catalog with descriptive column comments
- Never modify raw data after initial download — treat `data-source/` outputs as immutable

## Data Processing

- Every processing notebook/script starts by documenting: input tables (from Glue), transformations, output table
- Use Athena SQL or pandas/polars for transformations — choose based on data size
- Processing must be idempotent — re-running produces identical results
- Create one notebook or script per logical transformation step
- Organize into subfolders by domain or pipeline stage

## Schema Documentation

Every derived table must include a docstring or markdown cell explaining:

1. **Source tables** — Which Glue tables are queried
2. **Joins** — What keys are used, inner/left/outer
3. **Filters** — What rows are excluded and why
4. **Aggregations** — What level of granularity, what metrics
5. **Business logic** — Any domain-specific rules applied

## Anti-Patterns — NEVER Do

1. **Undocumented transformations** — every step must explain what and why
2. **Hardcoded S3 paths** — use config or environment variables
3. **Processing without schema validation** — check column types and nullability
4. **Skipping the Glue catalog** — all tables must be registered and discoverable
5. **Mixing download and processing** — keep `data-source/` and `data-processing/` separate
