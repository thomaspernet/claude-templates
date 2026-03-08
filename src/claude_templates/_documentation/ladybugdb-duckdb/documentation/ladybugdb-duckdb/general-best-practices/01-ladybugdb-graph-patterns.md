# LadybugDB Graph Patterns

> General best practices for modeling and querying property graphs with LadybugDB. Not specific to any application.

---

## When to Use a Graph vs. a Table

Use LadybugDB (graph) when:

- Relationships are first-class: who-knows-whom, part-of, depends-on
- You need path traversals: shortest path, reachability, N-hop neighbors
- The schema evolves around connections, not flat records
- You want graph algorithms: PageRank, community detection, connected components

Use DuckDB (relational/analytical) when:

- Data is naturally tabular: time series, logs, transactions
- You need aggregation-heavy analytics: GROUP BY, window functions, pivots
- Joins are simple (1-2 hops), not graph traversals

Many projects benefit from **both** — graph for relationships, DuckDB for analytics.

---

## Schema Design

### Node Tables

Every node table needs a PRIMARY KEY and clear purpose:

```cypher
CREATE NODE TABLE Person(
    id STRING PRIMARY KEY,
    name STRING,
    age INT64,
    created_at TIMESTAMP
);
```

Rules:
- One table per entity type — don't overload a single table with flags
- Use STRING PRIMARY KEY for UUIDs/external IDs, INT64 for auto-generated
- Keep property count reasonable (< 20) — split large schemas

### Relationship Tables

Relationships connect exactly two node tables with a direction:

```cypher
CREATE REL TABLE Follows(
    FROM Person TO Person,
    since DATE,
    weight DOUBLE
);

CREATE REL TABLE AuthoredBy(
    FROM Paper TO Person,
    contribution STRING
);
```

Rules:
- Name relationships as verbs: `WorksAt`, `Follows`, `BelongsTo`
- Store metadata on the relationship when it describes the connection
- A relationship table can only connect one pair of node types

### Modeling Checklist

1. Identify entities → node tables
2. Identify connections → relationship tables
3. Decide what properties live on nodes vs. relationships
4. Define primary keys
5. Plan indexes for common query patterns

---

## Query Patterns

### Pattern Matching

```cypher
-- Direct neighbors
MATCH (a:Person)-[:Follows]->(b:Person)
WHERE a.name = $name
RETURN b.name, b.age;

-- Multi-hop (friends of friends)
MATCH (a:Person)-[:Follows*2..3]->(b:Person)
WHERE a.name = $name
RETURN DISTINCT b.name;

-- Bidirectional (omit arrow for undirected search)
MATCH (a:Person)-[:Follows]-(b:Person)
WHERE a.name = $name
RETURN b.name;
```

### Aggregation

Cypher groups implicitly — no GROUP BY clause needed:

```cypher
MATCH (p:Person)-[:WorksAt]->(c:Company)
RETURN c.name, COUNT(p) AS headcount
ORDER BY headcount DESC;
```

### Subqueries with WITH

Use `WITH` to pipe intermediate results:

```cypher
MATCH (p:Person)-[:Follows]->(f:Person)
WITH p, COUNT(f) AS follower_count
WHERE follower_count > 10
RETURN p.name, follower_count;
```

### UNWIND for Bulk Operations

```cypher
UNWIND $items AS item
MERGE (p:Person {id: item.id})
SET p.name = item.name, p.age = item.age;
```

---

## Graph Algorithms (via extension)

```cypher
INSTALL algo; LOAD algo;
```

| Algorithm | Use Case |
|-----------|----------|
| PageRank | Node importance / influence |
| Shortest Path | Minimum hops between nodes |
| Connected Components | Cluster detection |
| K-Core Decomposition | Dense subgraph identification |
| Louvain | Community detection |

---

## Common Anti-Patterns

1. **Using graph for purely tabular data** — use DuckDB instead
2. **Unbounded traversals** — always limit depth: `[:Knows*1..4]`
3. **Giant node tables with 50+ properties** — split into focused tables
4. **Missing primary keys** — every node table needs one
5. **Modeling everything as a node** — some things are just properties
6. **String concatenation in queries** — always parameterize
