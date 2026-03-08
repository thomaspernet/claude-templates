# Performance and Scaling

> Best practices for performance tuning and scaling LadybugDB + DuckDB workloads. Not specific to any application.

---

## LadybugDB Performance

### Indexing

LadybugDB automatically indexes primary keys. For non-PK lookups, filter early:

```cypher
-- Good: filter on PK first, then traverse
MATCH (p:Person {id: $id})-[:Follows]->(f:Person)
RETURN f.name;

-- Bad: scan all persons, then filter
MATCH (p:Person)-[:Follows]->(f:Person)
WHERE p.name = $name
RETURN f.name;
```

### Query Profiling

```cypher
PROFILE MATCH (a:Person)-[:Knows*1..3]->(b:Person)
WHERE a.id = $id
RETURN b.name;
```

Look for:
- High row counts at early stages → add filters earlier
- Full scans → restructure query to use primary key lookups
- Cartesian products → ensure all MATCH patterns are connected

### Bulk Loading

Always use `COPY FROM` for initial data loads:

```python
# Fast: bulk load
conn.execute('COPY Person FROM "people.parquet"')

# Slow: row-by-row (100x slower for large datasets)
for person in people:
    conn.execute("CREATE (:Person {id: $id, name: $name})", person)
```

### Memory Management

- **On-disk mode** (`"file.lbug"`) for graphs larger than RAM
- **In-memory mode** (`":memory:"`) for small graphs or testing
- LadybugDB uses buffer pool management — it won't OOM on large graphs in on-disk mode

---

## DuckDB Performance

### Use Parquet

Parquet provides predicate pushdown and column pruning:

```sql
-- DuckDB only reads the 'amount' column and filters before loading
SELECT SUM(amount) FROM 'orders.parquet' WHERE date > '2024-01-01';
```

### Partition Large Datasets

```python
# Write partitioned Parquet
duck.execute("""
    COPY (SELECT * FROM orders)
    TO 'data/orders' (FORMAT PARQUET, PARTITION_BY (year, month))
""")

# Query only relevant partitions
duck.execute("SELECT * FROM 'data/orders/year=2024/month=03/*.parquet'")
```

### Profiling

```sql
EXPLAIN ANALYZE
SELECT region, SUM(amount) FROM orders GROUP BY region;
```

### Memory and Threads

```python
# Configure for your machine
conn = duckdb.connect(config={
    "threads": 8,
    "memory_limit": "4GB"
})
```

DuckDB spills to disk when memory_limit is exceeded — queries still complete, just slower.

---

## Scaling Guidelines

| Dataset Size | LadybugDB Mode | DuckDB Mode | Data Format |
|-------------|----------------|-------------|-------------|
| < 100K rows | In-memory | In-memory | CSV or Parquet |
| 100K–10M rows | On-disk | In-memory | Parquet |
| 10M–100M rows | On-disk | Persistent | Partitioned Parquet |
| > 100M rows | On-disk | Persistent | Partitioned Parquet + S3 |

---

## Monitoring Checklist

- [ ] Profile slow queries with `PROFILE` (LadybugDB) or `EXPLAIN ANALYZE` (DuckDB)
- [ ] Check that graph traversals have bounded depth
- [ ] Verify Parquet is used over CSV for repeated reads
- [ ] Monitor memory usage — switch to on-disk/persistent if approaching limits
- [ ] Benchmark bulk loads — `COPY FROM` should handle 1M+ rows/second
