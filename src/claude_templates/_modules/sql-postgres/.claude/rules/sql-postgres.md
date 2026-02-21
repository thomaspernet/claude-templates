# SQL / PostgreSQL Best Practices

## Query Style

- Keywords in UPPERCASE: `SELECT`, `FROM`, `WHERE`, `JOIN`, `ORDER BY`
- Table/column names in snake_case
- Always alias tables in JOINs: `FROM users u JOIN orders o ON u.id = o.user_id`
- One clause per line for readability
- Comment complex logic inline

```sql
SELECT
    u.id,
    u.email,
    COUNT(o.id) AS order_count
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01'
GROUP BY u.id, u.email
HAVING COUNT(o.id) > 5
ORDER BY order_count DESC
LIMIT 100;
```

## CTEs Over Subqueries

Use Common Table Expressions for readability and reuse:

```sql
WITH active_users AS (
    SELECT id, email FROM users WHERE status = 'active'
),
user_orders AS (
    SELECT user_id, COUNT(*) AS cnt FROM orders GROUP BY user_id
)
SELECT au.email, uo.cnt
FROM active_users au
JOIN user_orders uo ON au.id = uo.user_id;
```

## Window Functions

Use for running totals, ranking, partitioned aggregates:

```sql
SELECT
    id,
    amount,
    SUM(amount) OVER (ORDER BY created_at) AS running_total,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at DESC) AS rn
FROM orders;
```

## Indexing Strategy

- Index columns used in WHERE, JOIN, and ORDER BY
- Put most selective column first in composite indexes
- Don't over-index — each index slows writes
- Use `EXPLAIN ANALYZE` to verify query plans
- Partial indexes for common filtered subsets: `CREATE INDEX ... WHERE status = 'active'`
- Use `CONCURRENTLY` for index creation on live tables

## Connection Management

- Always use connection pooling (SQLAlchemy `pool_size=5`, `max_overflow=10`)
- Close connections explicitly or use context managers
- NEVER hardcode connection strings — use env vars
- Separate configs for dev / test / prod
- Use `statement_timeout` to prevent runaway queries

## Migrations

- One migration per logical change
- Always include a rollback (down migration)
- Test migrations on a copy before prod
- Never modify an already-applied migration
- Use `IF NOT EXISTS` / `IF EXISTS` for idempotent DDL

## Transactions

- Wrap multi-statement operations in explicit transactions
- Keep transactions short — long transactions hold locks
- Use `SAVEPOINT` for partial rollback within a transaction
- Set appropriate isolation level for your use case

## Anti-Patterns — NEVER Do

1. **SELECT \*** — specify columns explicitly
2. **N+1 queries** — use JOINs or batch fetches
3. **Missing indexes on JOIN/WHERE columns** — full table scans
4. **String concatenation for query building** — use parameterized queries
5. **Storing JSON blobs for queryable data** — normalize into columns
6. **No LIMIT on exploratory queries** — can return millions of rows
7. **Implicit type casting** — explicit `CAST()` prevents surprises
