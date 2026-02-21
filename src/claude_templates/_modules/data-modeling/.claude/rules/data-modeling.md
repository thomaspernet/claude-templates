# Data Modeling Best Practices

## General Principles

- Model the domain, not the UI — schemas should reflect business concepts
- Name things clearly: `user_accounts`, not `tbl_ua`; `created_at`, not `ca`
- Every table/node MUST have a primary key or unique identifier
- Prefer UUIDs over auto-increment IDs for distributed systems
- Include `created_at` and `updated_at` timestamps on all entities

## Relational (SQL) Modeling

### Normalization

Normalize to 3NF by default:

| Normal Form | Rule | Example |
|-------------|------|---------|
| 1NF | No repeating groups | Split comma-separated tags into a junction table |
| 2NF | No partial dependencies | Move order_date to orders table, not order_items |
| 3NF | No transitive dependencies | Move city_state to a separate addresses table |

### When to Denormalize

- Read-heavy analytics where JOINs are too expensive
- Caching materialized views for dashboards
- Embedding rarely-changing lookup values (country codes)
- Always document WHY you denormalized

### Naming Conventions

- Tables: plural snake_case (`user_accounts`, `order_items`)
- Columns: singular snake_case (`email`, `created_at`)
- Foreign keys: `{referenced_table_singular}_id` (`user_id`, `order_id`)
- Junction tables: `{table1}_{table2}` alphabetically (`orders_products`)
- Indexes: `idx_{table}_{columns}` (`idx_users_email`)

### Relationship Cardinality

Document every relationship:
- **1:1** — consider merging into one table unless separate concerns
- **1:N** — FK on the "many" side
- **N:M** — junction table with composite PK or surrogate key

## Graph (Neo4j) Modeling

### Nodes vs Relationships

- **Nodes**: entities with identity (Person, Document, Concept)
- **Relationships**: connections with meaning (AUTHORED, MENTIONS, RELATES_TO)
- If it can exist independently, it's a node
- If it only makes sense between two things, it's a relationship

### Property Placement

- Properties on nodes: attributes of the entity (name, type, created_at)
- Properties on relationships: attributes of the connection (weight, context, since)
- Don't store derived data that can be computed from graph traversal

### Labels

- Use PascalCase: `Person`, `Document`, `Tag`
- Use multiple labels for classification: `(:Person:Author)`
- Don't over-label — 2-3 labels per node is enough

## Schema Evolution

- Add columns/properties — safe, backward compatible
- Rename columns — requires migration and code update simultaneously
- Remove columns — mark as deprecated first, remove after confirming no usage
- Type changes — always add a new column, migrate data, then remove old
- Test migrations with production-like data volumes

## Anti-Patterns

1. **God table** — one table with 50+ columns for everything
2. **Entity-Attribute-Value (EAV)** — use JSONB or proper columns instead
3. **No foreign keys** — relying on application code for referential integrity
4. **Polymorphic associations** — a single FK pointing to multiple tables
5. **Premature denormalization** — normalize first, denormalize only when measured need
