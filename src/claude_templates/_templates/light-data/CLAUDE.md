# {PROJECT_NAME}

## Project & Tech

- **Language**: Python 3.10+
- **Graph database**: LadybugDB (embedded, Cypher queries)
- **Analytical database**: DuckDB (embedded, SQL queries)
- **Data formats**: Parquet (default), CSV (import), Arrow (in-memory transfer)
- **Package manager**: uv
- **Key directories**: `data/`, `src/`, `notebooks/`, `tests/`

## Architecture

```
data/
  raw/              Source files (CSV, JSON, Parquet)
  processed/        Cleaned, transformed data
  graph.lbug        LadybugDB graph database
  analytics.duckdb  DuckDB analytical database

src/
  models/           Schema definitions (node tables, rel tables, DuckDB tables)
  loaders/          Data loading scripts (bulk import, incremental)
  queries/          Reusable query functions (Cypher + SQL)
  pipelines/        ETL and transformation pipelines

notebooks/          Exploration and analysis notebooks
tests/              Unit + integration tests
```

## Dual-Engine Philosophy

Use each engine for what it does best:

- **LadybugDB** — relationships, traversals, graph algorithms (PageRank, shortest path, communities)
- **DuckDB** — aggregation, time series, analytical SQL, scanning Parquet/CSV files directly
- **Share data** via Apache Arrow (in-memory, zero-copy) or Parquet files (persistent)

Do NOT use DuckDB for graph traversals (recursive CTEs are slower). Do NOT use LadybugDB for heavy aggregation.

## Critical Rules

1. **Parameterized queries ALWAYS** — Never concatenate strings into Cypher or SQL. Use `$param` (Cypher) or `?` (DuckDB).
2. **Bulk load with COPY FROM** — Never loop individual CREATE/INSERT for large datasets.
3. **Parquet over CSV** — Convert source CSVs to Parquet once, then use Parquet for all reads.
4. **Every node table has a PRIMARY KEY** — No exceptions.
5. **Schema validation on all I/O** — Validate before loading, validate after transforming.
6. **NEVER hardcode file paths or connection strings** — Use config or env vars.
7. **Type hints on all functions** — Parameters and return types.

## Code Style

- `snake_case` for everything (Python, table names, column names)
- Cypher keywords in UPPERCASE: `MATCH`, `RETURN`, `WHERE`, `CREATE`
- SQL keywords in UPPERCASE: `SELECT`, `FROM`, `WHERE`, `JOIN`
- Early returns for validation failures
- One loader function per data source
- One query function per use case (not monolithic query files)
- **Prefer clarity and readability** over cleverness

## Dev Commands

```bash
uv run pytest                          # Run tests
uv run pytest tests/integration/       # Integration tests only
uv run python -m src.loaders.{name}    # Run a specific loader
uv run ruff check                      # Lint
uv run jupyter lab                     # Notebooks
```

## Testing

- **Unit tests**: Query functions with in-memory databases (`:memory:`)
- **Integration tests**: Full load → query → validate cycle with sample data
- **Schema tests**: Verify node/rel tables match expected structure
- Aim for 80%+ coverage on loaders and query functions

## Documentation — MANDATORY

This project may contain a `documentation/` folder organized by topic (like chapters of a book). Each topic subfolder has two sections:

```text
documentation/
  {topic}/
    general-best-practices/   — Industry reference (READ-ONLY, never modify)
    project-specific/          — This project's implementation (MUST stay in sync with code)
```

### Rules

1. **Never modify `general-best-practices/`.** These are reference benchmarks shipped with the project.
2. **Update `project-specific/` as part of every PR** that changes the topic area. If you add a node table, update the schema docs. If you change a pipeline, update the pipeline docs. Documentation updates are not optional — the work is incomplete without them.
3. **Read best practices before implementing.** Before building something new, read the relevant `general-best-practices/` doc and compare your design against it. Note intentional deviations in `project-specific/`.
4. **Keep inventories current.** If a `project-specific/` doc has an inventory table (tables, schemas, pipelines, etc.), it must match the codebase. Update it before starting new work if it's stale.
5. **Document decisions, not just code.** Explain *why* a schema choice or engine choice was made. Include dates for significant decisions.

## Workflow

- Commit prefixes: `fix:`, `feat:`, `refactor:`, `docs:`, `chore:`, `test:`
- NEVER force push without asking. NEVER commit credentials or database files.
- Add `*.lbug`, `*.duckdb`, and `data/` to `.gitignore`
- Test loaders against sample data before running on full datasets
- When compacting context, preserve: schema state, data issues found, query patterns discovered
