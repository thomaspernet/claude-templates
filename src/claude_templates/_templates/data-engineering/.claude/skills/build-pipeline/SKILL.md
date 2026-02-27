---
name: build-pipeline
description: "Use this skill when building a new data pipeline or ETL process. Invoke when the user describes ingesting data from a source, transforming records, loading to a warehouse or database, or scheduling a data job — even if they only describe the source and destination without calling it a pipeline."
---

# Build Pipeline

## When to Use

**Perfect for:**
- Building a new pipeline from a new data source
- Creating a new ETL workflow between existing systems
- Adding a new data flow to an existing pipeline module

**Not ideal for:**
- One-off data migrations (use a script, not a pipeline module)
- Ad-hoc queries or exploratory data pulls
- Schema-only changes or migrations (those belong in `models/`)

---

> **Core Philosophy:** A pipeline that cannot be re-run safely without side effects is broken by design. Idempotency is not a feature — it is the baseline requirement.

## ⚠️ CRITICAL

1. **Every load step MUST use UPSERT or MERGE, never INSERT.** A pipeline that uses INSERT will silently duplicate data on re-run. There are no exceptions to this rule.
2. **Schema validation on both ends.** Validate input schema before processing (fail fast on bad data). Validate output schema before writing (never write garbage to the target).
3. **Never hardcode connection strings.** All connection parameters come from env vars or config files. A hardcoded credential in pipeline code is a security incident.

---

## Step 1: Define Schema

- Input schema: source columns, types, constraints
- Output schema: target columns, types, constraints
- Mapping: how input maps to output

## Step 2: Write Extract

- Connect to data source
- Pull data with appropriate filters (date range, incremental key)
- Log row count
- Return raw DataFrame/records

## Step 3: Write Transform

- Pure function: DataFrame in → DataFrame out
- Apply business rules, type conversions, filtering
- Handle edge cases (nulls, duplicates, invalid values)
- Log input/output row counts

## Step 4: Write Load

- Validate output schema before writing
- Use UPSERT / MERGE for idempotency
- Use transactions for atomicity
- Log rows written

## Step 5: Add Validation

- Input schema validation (fail fast on bad data)
- Output quality checks (ranges, nulls, uniqueness)
- Row count sanity checks (not empty, not 10x expected)

## Step 6: Add Logging

- Pipeline start/end with duration
- Row counts at each step
- Error details with full context

## Step 7: Write Tests

- Unit tests for transform logic with sample data
- Integration test with test database
- Edge case tests (empty input, all nulls, duplicates)

## Output

Report the created files and confirm idempotency:

```
pipelines/{name}.py                          # Main module (extract/transform/load)
tests/unit/test_{name}.py                    # Transform unit tests
tests/integration/test_{name}_integration.py
```

Confirm: pipeline re-runs from scratch with no duplicate data.

## Checklist

- [ ] Extract pulls data correctly with filters
- [ ] Transform is a pure function, fully tested
- [ ] Load uses UPSERT/MERGE (idempotent)
- [ ] Schema validated on input and output
- [ ] No hardcoded connection strings
- [ ] Structured logging at every step
- [ ] Tests written and passing
- [ ] Pipeline re-runs safely from scratch
