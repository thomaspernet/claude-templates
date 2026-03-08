# LadybugDB Best Practices

## Overview

LadybugDB is an embedded graph database using Cypher. Use it as a lightweight alternative to Neo4j — no server, no Docker, just `pip install real_ladybug`.

- Embedded: runs in-process, zero deployment overhead
- Cypher query language (openCypher compatible)
- Columnar storage with compressed sparse row (CSR) adjacency lists
- Vectorized, multi-core query execution
- ACID transactions with write-ahead logging
- Native interop with Pandas, Polars, PyArrow, DuckDB

## Connection Patterns

```python
import real_ladybug as lb

# On-disk (persistent, handles larger-than-memory)
db = lb.Database("project.lbug")
conn = lb.Connection(db)

# In-memory (fast, no persistence)
db = lb.Database(":memory:")
conn = lb.Connection(db)

# Async (for FastAPI / async contexts)
conn = lb.AsyncConnection(db, max_concurrent_queries=4)
```

Always close connections when done. Use context managers or explicit cleanup.

## Schema Design

Define node and relationship tables with explicit types and primary keys:

```cypher
CREATE NODE TABLE Person(name STRING PRIMARY KEY, age INT64);
CREATE NODE TABLE Company(name STRING PRIMARY KEY, sector STRING);
CREATE REL TABLE WorksAt(FROM Person TO Company, since INT64, role STRING);
CREATE REL TABLE Knows(FROM Person TO Person, weight DOUBLE);
```

Rules:
- Every node table MUST have a PRIMARY KEY
- Use descriptive relationship names: `WorksAt`, `Knows`, `BelongsTo` — not `REL1`
- Store metadata on relationships when it describes the connection
- Keep node tables focused — split large schemas into separate tables

## Data Loading

Use `COPY FROM` for bulk loading — never loop `CREATE` for large datasets:

```python
# From CSV
conn.execute('COPY Person FROM "data/people.csv"')

# From Parquet
conn.execute('COPY Person FROM "data/people.parquet"')

# From Pandas/Polars DataFrame
conn.execute("COPY Person FROM df")

# Selective columns
conn.execute('COPY Person(name, age) FROM "partial.csv"')
```

Use `(header=false, ignore_errors=true)` options when needed. Check skipped rows with `CALL show_warnings()`.

## Query Patterns

### Basic MATCH

```cypher
MATCH (p:Person)-[w:WorksAt]->(c:Company)
WHERE p.age > 30
RETURN p.name, c.name, w.role
ORDER BY p.name;
```

### Parameterized Queries

ALWAYS use parameters. NEVER concatenate strings.

```python
conn.execute(
    "MATCH (p:Person {name: $name}) RETURN p.*",
    parameters={"name": user_input}
)
```

### Variable-Length Paths

```cypher
-- Friends of friends (2-3 hops)
MATCH (a:Person)-[:Knows*2..3]->(b:Person)
WHERE a.name = $name
RETURN DISTINCT b.name;
```

### Aggregation

Cypher uses implicit grouping — no explicit GROUP BY:

```cypher
MATCH (p:Person)-[:WorksAt]->(c:Company)
RETURN c.name, COUNT(p) AS headcount, AVG(p.age) AS avg_age
ORDER BY headcount DESC;
```

## Result Handling

```python
result = conn.execute("MATCH (p:Person) RETURN p.*")

# Iterate rows
for row in result:
    print(row)

# To Pandas
df = result.get_as_df()

# To Polars
pl_df = result.get_as_pl()

# To PyArrow
arrow = result.get_as_arrow()
```

## Extensions

Install extensions for additional capabilities:

```cypher
INSTALL duckdb;    LOAD duckdb;       -- DuckDB interop
INSTALL json;      LOAD json;         -- JSON scanning
INSTALL httpfs;    LOAD httpfs;       -- Remote file access (S3, HTTP)
INSTALL fts;       LOAD fts;          -- Full-text search (BM25)
```

Graph algorithms (PageRank, shortest paths, connected components, Louvain) are available via extension.

## DuckDB Integration

Query DuckDB tables directly from LadybugDB and vice versa:

```python
import duckdb
import real_ladybug as lb

# Both embedded — zero network overhead
duck = duckdb.connect("analytics.duckdb")
graph = lb.Database("graph.lbug")
conn = lb.Connection(graph)

# Load DuckDB query results into graph via Arrow
arrow_table = duck.execute("SELECT * FROM customers").fetch_arrow_table()
# Use LOAD FROM or COPY FROM with the Arrow table
```

Share data through Parquet files or Arrow tables — both databases handle them natively.

## Performance

- Load extensions with `LOAD` at session start (not per-query)
- Use `PROFILE` prefix to see execution plan and row counts
- Filter early with `WHERE` before traversing relationships
- Use `LIMIT` on exploratory queries
- Bulk load with `COPY FROM`, not individual `CREATE` statements
- For larger-than-memory graphs, use on-disk mode (`"project.lbug"`)

## Anti-Patterns — NEVER Do

1. **String concatenation in queries** — use parameters (`$name`, not f-strings)
2. **Individual CREATE in a loop** — use `COPY FROM` or `UNWIND` for bulk ops
3. **Missing PRIMARY KEY** — every node table needs one
4. **Unbounded traversals** — `[:Knows*]` without depth limit can explode; use `[:Knows*1..3]`
5. **Storing large blobs on nodes** — store in DuckDB or files, reference by ID
6. **Running Neo4j for small/embedded use cases** — LadybugDB is serverless and simpler
7. **Forgetting `LOAD extension`** — extensions must be loaded each session
