# Cypher / Neo4j Best Practices

## Query Patterns

### MERGE vs CREATE

- **MERGE** for idempotent writes — safely re-runnable, no duplicates
- **CREATE** only when you guarantee uniqueness or want duplicates
- Always specify enough properties in MERGE to uniquely identify the node

```cypher
-- Good: idempotent
MERGE (p:Person {uuid: $uuid})
SET p.name = $name, p.updated_at = datetime()

-- Bad: creates duplicates on re-run
CREATE (p:Person {name: $name})
```

### Parameterized Queries

ALWAYS use parameters. NEVER concatenate strings into queries.

```cypher
-- Good: parameterized
MATCH (n:Note {uuid: $uuid}) RETURN n

-- Bad: injection risk
MATCH (n:Note {uuid: '${user_input}'}) RETURN n
```

### Batch Operations

Use UNWIND for bulk operations instead of individual queries in a loop:

```cypher
UNWIND $items AS item
MERGE (n:Entity {uuid: item.uuid})
SET n.name = item.name, n.type = item.type
```

## Indexing

- Index properties used in MATCH and WHERE clauses
- Create indexes BEFORE bulk loading data
- Use composite indexes for multi-property lookups
- Check with `SHOW INDEXES` before creating duplicates

```cypher
CREATE INDEX note_uuid IF NOT EXISTS FOR (n:Note) ON (n.uuid)
CREATE INDEX entity_type_name IF NOT EXISTS FOR (e:Entity) ON (e.type, e.name)
```

## Relationship Patterns

- Relationships ALWAYS have a direction in CREATE/MERGE
- Direction is optional in MATCH (omit for bidirectional search)
- Use meaningful relationship types: `HAS_TAG`, `MENTIONS`, `RELATES_TO`
- Store metadata on relationships when it describes the connection

```cypher
MERGE (a)-[:MENTIONS {context: $context, weight: $weight}]->(b)
```

## Performance

- Use `PROFILE` to see execution plan and actual row counts
- Use `EXPLAIN` to see plan without executing
- Avoid unbounded queries — always use LIMIT or WHERE constraints
- Use `WITH` to reduce cardinality early in multi-part queries
- Avoid `OPTIONAL MATCH` when you can use `MATCH` — it's slower

```cypher
-- Good: filter early
MATCH (n:Note)
WHERE n.created_at > $since
WITH n LIMIT 100
MATCH (n)-[:HAS_TAG]->(t:Tag)
RETURN n, collect(t) AS tags

-- Bad: unbounded, then filter late
MATCH (n:Note)-[:HAS_TAG]->(t:Tag)
WHERE n.created_at > $since
RETURN n, collect(t) AS tags
```

## APOC Utilities

- `apoc.periodic.iterate` for large batch operations
- `apoc.merge.node` for dynamic label/property merges
- `apoc.create.uuid()` for generating UUIDs in queries
- `apoc.text.fuzzyMatch` for fuzzy string matching

## Anti-Patterns — NEVER Do

1. **String concatenation in queries** — use parameters
2. **Unbounded MATCH without LIMIT** — can return millions of rows
3. **CREATE instead of MERGE for upserts** — creates duplicates
4. **Missing indexes on MATCH properties** — full graph scan
5. **Storing large text blobs on nodes** — use separate storage, reference by ID
6. **Cartesian products** — unconnected MATCH clauses multiply results
