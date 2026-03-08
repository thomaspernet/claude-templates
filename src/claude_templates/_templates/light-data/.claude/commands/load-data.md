Load data into the project databases.

Steps:
1. Check what source files exist in `data/raw/`
2. Identify the target — LadybugDB (graph) or DuckDB (analytics) based on the data shape
3. For graph data: define node/rel tables if they don't exist, then `COPY FROM`
4. For analytical data: create DuckDB table or query Parquet directly
5. Validate row counts and schema after loading
6. Update `documentation/ladybugdb-duckdb/project-specific/01-overview.md` schema inventory
