# LadybugDB + DuckDB Documentation — Mandatory Maintenance

This project maintains structured documentation in `documentation/ladybugdb-duckdb/`. Keeping it current is **not optional** — it is part of every feature, refactor, and bugfix that touches graph models, analytical queries, or data pipelines.

## Folder Structure

```
documentation/ladybugdb-duckdb/
  general-best-practices/   — Industry best practices (READ-ONLY reference)
  project-specific/          — This project's implementation (MUST be kept in sync with code)
```

## Rules

### 1. Never modify `general-best-practices/`

These are reference documents shipped with the project template. Treat them as read-only benchmarks. If you disagree with a practice, document the deviation in `project-specific/`, do not edit the original.

### 2. Documentation updates are mandatory, not optional

Every PR or commit that changes graph schema, analytical queries, or data pipelines MUST include corresponding documentation updates. This applies to:

- Adding, removing, or changing node/relationship tables
- Adding or modifying DuckDB tables or views
- Changing data loading pipelines (CSV, Parquet, Arrow)
- Adding graph algorithms or analytical queries
- Modifying the interop layer between LadybugDB and DuckDB
- Fixing a bug that reveals a pattern worth documenting

If the code change touches data models or queries and the PR does not update `documentation/ladybugdb-duckdb/project-specific/`, the work is incomplete.

### 3. Read best practices before implementing

Before implementing a new data model, query, or pipeline, read the relevant doc in `general-best-practices/`:

| Task | Read first |
|------|-----------|
| New graph model | `01-ladybugdb-graph-patterns.md` — schema, relationships, traversals |
| New analytical query | `02-duckdb-analytical-patterns.md` — SQL, window functions, aggregation |
| Data pipeline / loading | `03-data-interop.md` — Arrow, Parquet, cross-database patterns |
| Performance work | `04-performance-and-scaling.md` — indexing, profiling, memory |

Note intentional deviations from best practices in the project-specific docs with a brief rationale.

### 4. Keep the schema inventory current

The schema inventory in `project-specific/01-overview.md` is the source of truth for what node tables, relationship tables, and DuckDB tables exist. Before starting new data work:

1. Check if the inventory matches the codebase
2. If it doesn't, update it first
3. Then proceed with the new work

### 5. What to document

| Change | Update |
|--------|--------|
| New node/rel table | `01-overview.md` schema inventory |
| New DuckDB table/view | `01-overview.md` schema inventory |
| New query pattern | `02-patterns.md` with example |
| Architecture change | `01-overview.md` with date and rationale |
| Anti-pattern discovered | `02-patterns.md` with explanation |
| Pipeline change | `01-overview.md` data flow section |

### 6. Documentation quality standards

- **Be specific.** Reference actual table names, column types, query patterns — not abstract descriptions.
- **Show code.** Include Cypher and SQL examples of correct implementations.
- **Date decisions.** When documenting a schema choice, include the date and rationale.
- **Keep it concise.** If a section exceeds 200 lines, split it.
