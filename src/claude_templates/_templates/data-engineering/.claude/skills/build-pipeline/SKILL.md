---
name: build-pipeline
description: "Step-by-step ETL pipeline construction. Use when creating a new data pipeline."
---

# Build Pipeline

Follow these steps to create a new data pipeline.

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

## Checklist

- [ ] Extract pulls data correctly
- [ ] Transform logic is pure and tested
- [ ] Load uses upserts (idempotent)
- [ ] Schema validated on input and output
- [ ] Logging at every step
- [ ] Tests written and passing
- [ ] Pipeline is re-runnable safely
