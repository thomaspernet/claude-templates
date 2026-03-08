---
paths:
  - "**/src/**"
  - "**/data/**"
  - "**/notebooks/**"
---

# Data Conventions

## LadybugDB (Graph)

- Import as `import real_ladybug as lb`
- On-disk for persistent data: `lb.Database("data/graph.lbug")`
- In-memory for tests: `lb.Database(":memory:")`
- Always parameterize: `conn.execute("MATCH (n {id: $id}) ...", parameters={"id": val})`
- Bulk load: `conn.execute('COPY TableName FROM "file.parquet"')`
- Results to DataFrame: `result.get_as_df()` (Pandas) or `result.get_as_pl()` (Polars)

## DuckDB (Analytics)

- Import as `import duckdb`
- Query files directly: `duckdb.sql("SELECT * FROM 'data/file.parquet'")`
- Parameterize: `conn.execute("SELECT * WHERE id = ?", [val])`
- Use QUALIFY for window-filtered queries (no subquery needed)
- Prefer Parquet over CSV for all repeated reads

## Data Flow Between Engines

- Arrow for in-memory transfer (zero-copy, fastest)
- Parquet for persistent interchange
- Never duplicate data in both engines — store once, query via interop

## File Organization

- `data/raw/` — untouched source files
- `data/processed/` — transformed, ready for loading
- One loader per source in `src/loaders/`
- One query module per domain in `src/queries/`
