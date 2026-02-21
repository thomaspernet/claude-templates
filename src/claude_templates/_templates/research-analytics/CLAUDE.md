# {PROJECT_NAME}

## Project & Tech

- **Type**: Academic research repository — all code, data, and analysis that produce a paper
- **Language**: Python, managed with `uv`
- **Data infrastructure**: AWS Athena (S3 + Glue catalog)
- **Data downloads**: [`aws-python`](https://github.com/thomaspernet/aws-python) patterns
- **Analysis**: Jupyter notebooks, pandas, polars, matplotlib, seaborn, plotly

## Architecture

```
data-source/        Download external data, save to S3/Athena via Glue
data-processing/    Query Athena, process, enrich, create derived tables
data-analysis/      Figures and tables for the paper
src/                Shared utility modules (imported by notebooks)
```

### `data-source/`

Scripts that download raw data from external providers and register it in the Glue catalog. Each script should document: where the data comes from, what it contains, and how it maps to Glue tables. Follow `aws-python` patterns for S3 uploads and Glue registration.

### `data-processing/`

Notebooks and scripts that query Athena, join, filter, aggregate, and enrich data into analysis-ready tables. Each processing step must document: input tables, transformations applied, and output table schema.

### `data-analysis/`

Analysis notebooks that produce the figures and tables for the paper. Maintain a **single source-of-truth notebook** that contains all tables referenced in the paper. Additional notebooks for exploratory analysis or individual figures.

## Critical Rules

1. **Explain process, never code** — When describing a table or figure, explain the data flow (source → processing → output), not the Python implementation.
2. **Full transparency** — Always trace results back to their source. Reference `data-source/` scripts, `data-processing/` steps, and Glue catalog definitions.
3. **Single source of truth** — All paper tables live in one notebook in `data-analysis/`. This is the canonical reference.
4. **Extract code to modules** — Keep notebooks lean. Reusable logic goes in `src/`. Use `%load_ext autoreload` / `%autoreload 2` at the top of every notebook.
5. **Notebooks are documents** — Markdown cells explain intent and interpret results. Short paragraphs, academic tone. Prefer tables and figures over print statements.
6. **Data provenance is mandatory** — Every derived table must document: source tables, joins, filters, and business logic applied.
7. **Reproducibility** — Every result must be regenerable from raw data + code.

## Code Style

- `snake_case` everywhere (variables, functions, files)
- Type hints on all functions in `src/`
- **Prefer clarity and readability** over cleverness in all code
- Organize code into **folders and subfolders** by domain — avoid many files under the same directory
- Markdown cells explain the **why**, code cells do the **what**
- Keep notebook cells short — one logical step per cell

## Dev Commands

```bash
uv run pytest                  # Run tests for src/ modules
uv run jupyter lab             # Launch notebook environment
uv run ruff check              # Lint Python files
```

## Testing

- `pytest` for all functions in `src/`
- Notebooks validated by executing top-to-bottom with `jupyter nbconvert --execute`
- Test edge cases: empty DataFrames, NaN values, type mismatches

## Workflow

- Conventional commits: `fix:`, `feat:`, `refactor:`, `docs:`, `chore:`, `test:`
- Reproducibility first — every result must be regenerable from raw data + code
- Commit notebooks with cleared outputs unless they serve as reports
- When compacting context, preserve: paper structure, table provenance, data issues found, processing decisions
