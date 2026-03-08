# Project-Specific Data Documentation

This folder tracks how **this project** uses LadybugDB and DuckDB. It serves as both a human-readable reference and a benchmark the coding agent uses when implementing or modifying data models and queries.

## How to Use This Folder

1. **Create files that document your project's current state** — graph schema, analytical tables, data pipelines, query patterns.
2. **Reference the general best practices** in `../general-best-practices/` as the benchmark.
3. **Keep docs in sync with code** — update this folder whenever you add, change, or remove data models or queries.

## Suggested Structure

Start with the files that match your project's scope. Not all are needed.

| File | Purpose | When to Create |
|------|---------|----------------|
| `01-overview.md` | Architecture, schema inventory, data flow | Always — start here |
| `02-patterns.md` | Project-specific query patterns and conventions | When you have established patterns |
| `03-pipelines.md` | Data loading and transformation pipelines | When you have ETL workflows |
| `04-decisions.md` | Architectural decisions log (what, when, why) | When making non-obvious choices |

## Writing Guidelines

- **Be specific.** Reference actual table names, column types, file paths.
- **Show the query, not just the rule.** Include Cypher and SQL examples.
- **Date your decisions.** Note when schema choices were made and why.
- **Keep it concise.** If a section exceeds 200 lines, split it.
