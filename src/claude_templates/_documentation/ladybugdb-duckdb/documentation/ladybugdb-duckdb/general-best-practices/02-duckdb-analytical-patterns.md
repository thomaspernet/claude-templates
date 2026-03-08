# DuckDB Analytical Patterns

> General best practices for analytical queries with DuckDB. Not specific to any application.

---

## Why DuckDB

DuckDB is an embedded analytical database — the SQLite of OLAP:

- In-process, zero deployment (just `pip install duckdb`)
- Columnar storage, vectorized execution
- Reads Parquet, CSV, JSON, Arrow natively — no ETL needed
- SQL with modern extensions (QUALIFY, PIVOT, list comprehensions)

---

## Connection Patterns

```python
import duckdb

# In-memory (default, fast, no persistence)
conn = duckdb.connect()

# Persistent (on-disk)
conn = duckdb.connect("analytics.duckdb")

# Read-only (safe for concurrent readers)
conn = duckdb.connect("analytics.duckdb", read_only=True)
```

---

## Querying External Files Directly

No loading required — query files in place:

```sql
-- Parquet (local or S3)
SELECT * FROM 'data/events.parquet' WHERE event_type = 'purchase';

-- CSV with auto-detection
SELECT * FROM read_csv_auto('data/users.csv');

-- Multiple files via glob
SELECT * FROM 'data/logs/*.parquet';

-- JSON
SELECT * FROM read_json_auto('data/config.json');
```

---

## Core SQL Patterns

### CTEs for Readability

```sql
WITH daily_revenue AS (
    SELECT
        date_trunc('day', created_at) AS day,
        SUM(amount) AS revenue
    FROM orders
    GROUP BY 1
)
SELECT day, revenue,
    AVG(revenue) OVER (ORDER BY day ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS rolling_7d
FROM daily_revenue
ORDER BY day;
```

### Window Functions

```sql
SELECT
    user_id,
    order_date,
    amount,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY order_date) AS order_num,
    SUM(amount) OVER (PARTITION BY user_id ORDER BY order_date) AS cumulative_spend,
    LAG(order_date) OVER (PARTITION BY user_id ORDER BY order_date) AS prev_order
FROM orders;
```

### QUALIFY (DuckDB extension)

Filter on window functions without nesting:

```sql
-- Latest order per user (no subquery needed)
SELECT *
FROM orders
QUALIFY ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY order_date DESC) = 1;
```

### PIVOT / UNPIVOT

```sql
PIVOT orders ON status USING COUNT(*) GROUP BY region;
```

### List and Struct Operations

```sql
SELECT
    user_id,
    LIST(product_name) AS products,
    LIST(amount ORDER BY amount DESC) AS amounts_sorted
FROM orders
GROUP BY user_id;
```

---

## DataFrame Interop

```python
import pandas as pd
import polars as pl

# Query a Pandas DataFrame directly
df = pd.read_csv("users.csv")
result = duckdb.sql("SELECT * FROM df WHERE age > 30")

# Return as Polars
pl_df = result.pl()

# Return as Arrow
arrow = result.arrow()

# Return as Pandas
pandas_df = result.df()
```

---

## Performance Tips

- **Parquet over CSV** — columnar format, predicate pushdown, much faster
- **Partitioned Parquet** — partition by date/category for selective reads
- **Avoid SELECT *** — specify columns to benefit from columnar pruning
- **Use EXPLAIN ANALYZE** to profile slow queries
- **Persistent mode** for data > RAM — DuckDB spills to disk automatically
- **Parallel reads** — DuckDB parallelizes file reads and query execution automatically

---

## Anti-Patterns — NEVER Do

1. **Loading CSVs into tables when you can query them directly** — DuckDB reads files natively
2. **Using DuckDB for OLTP workloads** — it's analytical, not transactional
3. **SELECT * on large datasets without LIMIT** — always bound exploratory queries
4. **Ignoring Parquet** — if you're reading CSVs repeatedly, convert to Parquet once
5. **String formatting SQL** — use parameterized queries: `conn.execute("... WHERE id = ?", [user_id])`
6. **Storing graph relationships in flat tables** — use LadybugDB for graph traversals
