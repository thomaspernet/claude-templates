# Validate Pipeline

Run a pipeline in test/dry-run mode and check data quality.

## Steps

1. **Identify pipeline** — Which pipeline to validate.
2. **Check config** — Verify all required env vars / config values are set.
3. **Run extract** — Pull sample data (limit to 1000 rows for validation).
4. **Validate input schema** — Check column names, types, nulls against expected schema.
5. **Run transform** — Apply transformations to sample data.
6. **Validate output schema** — Check result matches expected output schema.
7. **Data quality checks**:
   - No unexpected nulls in required columns
   - Values within expected ranges
   - No duplicate primary keys
   - Row count within expected bounds
8. **Report** — Summary of all checks with pass/fail status.

Do NOT write to production databases during validation.
