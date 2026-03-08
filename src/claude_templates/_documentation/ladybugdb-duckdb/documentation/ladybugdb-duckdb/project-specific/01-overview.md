# Project Data Architecture Overview

> Document your project's data architecture here. This file should be the first place a developer or coding agent looks to understand how data flows in this project.

---

## Architecture

<!-- Describe how your project uses LadybugDB and DuckDB. Example: -->

```
TODO: Replace with your project's data architecture

data/
  raw/              — Source files (CSV, JSON, Parquet)
  processed/        — Cleaned / transformed data
  graph.lbug        — LadybugDB graph database
  analytics.duckdb  — DuckDB analytical database

src/
  models/           — Schema definitions
  loaders/          — Data loading scripts
  queries/          — Reusable query functions
  pipelines/        — ETL / transformation pipelines
```

---

## Graph Schema (LadybugDB)

<!-- List all node and relationship tables. Keep this inventory current. -->

| Table | Type | Primary Key | Properties | Purpose |
|-------|------|-------------|------------|---------|
| `Person` | Node | `id STRING` | name, age, created_at | Example — replace |
| `Follows` | Rel | Person → Person | since, weight | Example — replace |

---

## Analytical Tables (DuckDB)

<!-- List all DuckDB tables and views. -->

| Table/View | Type | Source | Purpose |
|------------|------|--------|---------|
| `events` | Table | `data/events.parquet` | Example — replace |
| `daily_summary` | View | Derived from events | Example — replace |

---

## Data Flow

<!-- Describe how data moves between sources, LadybugDB, and DuckDB. -->

```
TODO: Replace with your data flow

Source files → DuckDB (clean, aggregate) → Parquet → LadybugDB (graph model)
                                         ↓
                                    Analytics queries
```

---

## Key Query Patterns

<!-- Document the most important queries your project runs. -->

| Query | Engine | Purpose |
|-------|--------|---------|
| TODO | LadybugDB | Example graph traversal |
| TODO | DuckDB | Example analytical query |

---

## Adding New Data

Checklist:

- [ ] Define schema (node/rel table or DuckDB table)
- [ ] Update inventory tables above
- [ ] Write loader script in `loaders/`
- [ ] Add validation/tests
- [ ] Document data source and refresh frequency
