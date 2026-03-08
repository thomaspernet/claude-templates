# Data Interop: LadybugDB + DuckDB

> Best practices for sharing data between LadybugDB (graph) and DuckDB (analytics). Not specific to any application.

---

## Architecture: Two Embedded Engines

Both databases run in-process with zero network overhead:

```
Your Python Application
├── LadybugDB (graph.lbug)   — relationships, traversals, graph algorithms
├── DuckDB (analytics.duckdb) — aggregation, time series, analytical SQL
└── Shared data via Arrow / Parquet
```

The key insight: **use each engine for what it does best**, share data through Arrow or Parquet.

---

## Sharing Data via Apache Arrow

Arrow is the fastest path — zero-copy in-memory transfer:

```python
import real_ladybug as lb
import duckdb

graph_db = lb.Database("graph.lbug")
graph = lb.Connection(graph_db)
duck = duckdb.connect("analytics.duckdb")

# LadybugDB → DuckDB (graph results into analytics)
arrow_table = graph.execute(
    "MATCH (p:Person)-[:WorksAt]->(c:Company) RETURN p.name, c.name AS company"
).get_as_arrow()
duck.execute("CREATE TABLE employees AS SELECT * FROM arrow_table")

# DuckDB → LadybugDB (analytical results into graph)
arrow_table = duck.execute(
    "SELECT id, name, category FROM products"
).fetch_arrow_table()
# Load into LadybugDB via DataFrame/Arrow scanning
```

---

## Sharing Data via Parquet

For persistent interchange or when datasets are large:

```python
# DuckDB → Parquet → LadybugDB
duck.execute("COPY (SELECT * FROM customers) TO 'data/customers.parquet'")
graph.execute("COPY Customer FROM 'data/customers.parquet'")

# LadybugDB → Parquet → DuckDB
# Export graph query results, then read in DuckDB
df = graph.execute("MATCH (p:Person) RETURN p.*").get_as_df()
df.to_parquet("data/people.parquet")
duck.execute("CREATE TABLE people AS SELECT * FROM 'data/people.parquet'")
```

---

## When to Use Which Engine

| Task | Use | Why |
|------|-----|-----|
| "Who are X's connections?" | LadybugDB | Graph traversal |
| "What's the average order value by region?" | DuckDB | Aggregation |
| "Find shortest path between A and B" | LadybugDB | Graph algorithm |
| "Show monthly revenue trend" | DuckDB | Time series analytics |
| "Which communities exist in the network?" | LadybugDB | Louvain/components |
| "Join 3 tables and compute percentiles" | DuckDB | Complex SQL |
| "Find all entities within 3 hops of X" | LadybugDB | Path traversal |
| "Scan 10M rows of logs for anomalies" | DuckDB | Columnar scan |

---

## Common Interop Patterns

### Pattern 1: Graph-Enriched Analytics

Run graph algorithm, then analyze results in DuckDB:

```python
# 1. Compute PageRank in LadybugDB
ranks = graph.execute("""
    MATCH (p:Person)
    RETURN p.id, p.name, p.pagerank
""").get_as_arrow()

# 2. Join with transactional data in DuckDB
duck.execute("""
    CREATE TABLE person_ranks AS SELECT * FROM ranks;
    SELECT pr.name, pr.pagerank, SUM(o.amount) AS total_spend
    FROM person_ranks pr
    JOIN orders o ON pr.id = o.customer_id
    GROUP BY pr.name, pr.pagerank
    ORDER BY pr.pagerank DESC;
""")
```

### Pattern 2: Analytics-Driven Graph Loading

Aggregate in DuckDB, load summary into graph:

```python
# 1. Aggregate interactions in DuckDB
duck.execute("""
    COPY (
        SELECT sender_id, receiver_id, COUNT(*) AS weight
        FROM messages
        GROUP BY sender_id, receiver_id
        HAVING COUNT(*) >= 5
    ) TO 'data/edges.parquet'
""")

# 2. Load as relationships in LadybugDB
graph.execute("COPY Communicates FROM 'data/edges.parquet'")
```

### Pattern 3: Dual Query

Query both engines and merge in Python:

```python
# Graph: get network neighborhood
neighbors = graph.execute("""
    MATCH (a:Person {id: $id})-[:Knows*1..2]->(b:Person)
    RETURN DISTINCT b.id
""", parameters={"id": target_id}).get_as_df()

# Analytics: get details for those neighbors
ids = neighbors["b.id"].tolist()
details = duck.execute("""
    SELECT * FROM user_profiles WHERE id = ANY(?)
""", [ids]).df()
```

---

## File Format Recommendations

| Format | When to Use |
|--------|------------|
| **Parquet** | Default for persistent interchange — columnar, compressed, fast |
| **Arrow** | In-memory transfer between engines — zero-copy, fastest |
| **CSV** | Initial data import, human-readable debugging |
| **JSON** | Nested/semi-structured source data |

---

## Anti-Patterns

1. **Duplicating data in both engines** — store once, query via interop
2. **Using DuckDB for graph traversals** — recursive CTEs are slower than native graph
3. **Using LadybugDB for heavy aggregation** — DuckDB's columnar engine is faster
4. **Converting Arrow → CSV → Arrow** — keep data in Arrow/Parquet format
5. **Running both engines on the same file simultaneously** — use separate files or in-memory transfer
