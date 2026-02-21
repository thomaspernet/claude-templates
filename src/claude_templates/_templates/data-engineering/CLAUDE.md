# {PROJECT_NAME}

## BUGS.md and MISTAKES.md — READ AND UPDATE (MANDATORY)

1. **START OF SESSION**: Read `BUGS.md` and `MISTAKES.md` before making any changes.
2. **WHEN YOU HIT A BUG**: Add entry to `BUGS.md` BEFORE attempting the fix.
3. **WHEN YOU MAKE A MISTAKE**: Add entry to `MISTAKES.md` BEFORE fixing it.
4. **WHEN YOU FIX A BUG**: Update the entry status to FIXED with root cause.

## Project & Tech

- **Language**: Python (SQLAlchemy, Prefect, dbt, Great Expectations)
- **Databases**: PostgreSQL / Neo4j / {DATABASE}
- **Package manager**: uv
- **Key directories**: `pipelines/`, `models/`, `tests/`, `config/`

## Architecture

```
pipelines/          ETL pipeline modules (one per data flow)
models/             SQLAlchemy models or dbt models
tests/              Unit + integration tests
config/             YAML/env configuration files
scripts/            One-off maintenance scripts
```

Each pipeline is a self-contained module: extract → transform → load.

## Critical Rules

1. **Idempotent pipelines** — Every pipeline MUST be safely re-runnable. Use upserts, not inserts.
2. **Schema validation on all I/O** — Validate input schema before processing, output schema before writing.
3. **NEVER hardcode connection strings** — Use env vars or config files.
4. **Log every pipeline step** — Start, end, row counts, errors. Use structured logging.
5. **Handle partial failures** — If step 3/5 fails, don't lose steps 1-2. Use checkpoints or transactions.
6. **Each task gets its own DB connector** — NEVER share connections between concurrent tasks.
7. **Type hints on all functions** — Parameters and return types.

## Code Style

- Pipeline functions are pure transforms (input → output)
- Side effects (DB writes, API calls) isolated at boundaries
- Config via env vars or YAML — never hardcoded
- `snake_case` for everything
- Early returns for validation failures
- **Prefer clarity and readability** over cleverness in all code
- Organize pipelines into **folders and subfolders** by domain — avoid many files under the same directory

## Dev Commands

```bash
uv run pytest                          # Run tests
uv run pytest tests/integration/       # Integration tests only
uv run prefect server start            # Start Prefect UI
uv run python -m pipelines.{name}      # Run a specific pipeline
uv run ruff check                      # Lint
```

## Testing

- **Unit tests**: Pure transform functions with sample data
- **Integration tests**: Against test database (separate from prod)
- **Data quality**: Great Expectations or custom validators on pipeline output
- Aim for 80%+ coverage on transform logic

## Workflow

- Commit prefixes: `fix:`, `feat:`, `refactor:`, `docs:`, `chore:`, `test:`
- NEVER force push without asking. NEVER commit credentials.
- Test pipelines against sample data before running on production
- When compacting context, preserve: pipeline state, data issues found, schema decisions
