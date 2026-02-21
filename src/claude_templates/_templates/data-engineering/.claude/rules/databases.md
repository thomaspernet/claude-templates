---
paths:
  - "**/models/**"
  - "**/migrations/**"
  - "**/*.sql"
---

# Database Rules

## SQL Style

- Keywords in UPPERCASE: `SELECT`, `FROM`, `WHERE`, `JOIN`
- Table/column names in snake_case
- Always alias tables in JOINs: `FROM users u JOIN orders o ON u.id = o.user_id`
- One clause per line for readability
- Comment complex queries inline

## Migrations

- One migration per logical change
- Always include a rollback (down migration)
- Test migrations against a copy before running on prod
- Never modify a migration that has already been applied

## Connection Management

- Use connection pooling (SQLAlchemy `create_engine(pool_size=5)`)
- Close connections explicitly or use context managers
- NEVER hardcode connection strings — use env vars
- Separate connection configs for dev / test / prod

## Indexing

- Index columns used in WHERE, JOIN, and ORDER BY
- Don't over-index — each index slows writes
- Use EXPLAIN ANALYZE to verify query plans
- Composite indexes: put most selective column first

## Neo4j / Cypher

- Use parameterized queries — NEVER string-concatenate values
- Use MERGE for idempotent writes
- Index properties used in MATCH lookups
- Use UNWIND for batch operations instead of loops
