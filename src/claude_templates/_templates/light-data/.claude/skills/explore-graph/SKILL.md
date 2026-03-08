---
name: explore-graph
description: "Use this skill to explore and understand a LadybugDB graph: discover schema, sample data, compute basic statistics, and run graph algorithms."
---

# Explore Graph

## When to Use

When you need to understand the structure and content of a LadybugDB graph database — what nodes exist, how they're connected, key statistics, and interesting patterns.

## Steps

### 1. Discover Schema

```cypher
CALL TABLE_INFO('*') RETURN *;
```

List all node and relationship tables with their properties.

### 2. Sample Data

For each node table:
```cypher
MATCH (n:TableName) RETURN n.* LIMIT 10;
```

For each relationship table:
```cypher
MATCH (a)-[r:RelName]->(b) RETURN a.*, r.*, b.* LIMIT 10;
```

### 3. Compute Statistics

```cypher
-- Node counts per table
MATCH (n:TableName) RETURN COUNT(n);

-- Relationship counts
MATCH ()-[r:RelName]->() RETURN COUNT(r);

-- Degree distribution (how connected are nodes?)
MATCH (n:TableName)-[r]->()
RETURN n.id, COUNT(r) AS out_degree
ORDER BY out_degree DESC LIMIT 20;
```

### 4. Explore Connectivity

```cypher
-- Connected components (if algo extension loaded)
-- Shortest paths between notable nodes
-- Community structure
```

### 5. Cross-Reference with DuckDB

If analytical data exists, join graph results with DuckDB tables via Arrow:

```python
arrow = conn.execute("MATCH (n:Person) RETURN n.*").get_as_arrow()
duck.execute("SELECT * FROM arrow WHERE age > 30")
```

### 6. Summarize Findings

Report:
- Number of node/relationship tables and their sizes
- Key structural patterns (star graphs, chains, clusters)
- Notable outliers (highly connected nodes, isolated nodes)
- Recommendations for graph algorithms to run
