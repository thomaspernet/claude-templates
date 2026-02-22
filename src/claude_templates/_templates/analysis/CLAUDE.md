# {PROJECT_NAME}

## Project & Tech

- **Language**: Python, managed with `uv`
- **Libraries**: pandas, polars, matplotlib, seaborn, plotly, scikit-learn
- **Notebooks**: Jupyter for exploration, processing, and presentation
- **Data formats**: CSV, Parquet, JSON, or cloud storage (S3/Athena optional)

## Architecture

```
data-source/        Download or collect raw data from external providers
data-processing/    Clean, transform, enrich, create analysis-ready datasets
data-analysis/      Figures, tables, and final analysis notebooks
src/                Shared utility modules (imported by notebooks)
```

### `data-source/`

Scripts and notebooks that acquire raw data. Each must document: where the data comes from, what it contains, and how it is stored. Raw data is immutable once downloaded — never modify source files.

### `data-processing/`

Notebooks and scripts that clean, join, filter, aggregate, and enrich data into analysis-ready datasets. Each processing step must document: input data, transformations applied, and output schema.

### `data-analysis/`

Analysis notebooks that produce the figures and tables. Maintain a **single source-of-truth notebook** for key results. Additional notebooks for exploratory analysis or individual figures.

## Critical Rules

1. **Explain process, never code** — When describing a result, explain the data flow (source → processing → output), not the Python implementation.
2. **Full transparency** — Always trace results back to their source. Reference `data-source/` scripts and `data-processing/` steps.
3. **Single source of truth** — Key results live in one notebook in `data-analysis/`. This is the canonical reference.
4. **Extract code to modules** — Keep notebooks lean. Reusable logic goes in `src/`. Use `%load_ext autoreload` / `%autoreload 2` at the top of every notebook.
5. **Notebooks are documents** — Markdown cells explain intent and interpret results. Short paragraphs, academic tone. Prefer tables and figures over print statements.
6. **Data provenance is mandatory** — Every derived dataset must document: source data, joins, filters, and logic applied.
7. **Reproducibility** — Every result must be regenerable from raw data + code. Pin random seeds (`random_state=42`). Always specify `dtype` when reading data files.

## Code Style

- `snake_case` everywhere (variables, functions, files)
- Type hints on all functions in `src/`
- Docstrings with parameter descriptions on all public functions
- **Prefer clarity and readability** over cleverness in all code
- Organize code into **folders and subfolders** by domain — avoid many files under the same directory
- Markdown cells explain the **why**, code cells do the **what**
- Keep notebook cells short — one logical step per cell

## Dev Commands

```bash
uv run pytest              # Run tests for src/ modules
uv run jupyter lab         # Launch notebook environment
uv run ruff check          # Lint Python files
```

## Testing

- `pytest` for all functions in `src/`
- Notebooks validated by executing top-to-bottom with `jupyter nbconvert --execute`
- Test edge cases: empty DataFrames, NaN values, type mismatches

## Documentation — MANDATORY

This project may contain a `documentation/` folder organized by topic (like chapters of a book). Each topic subfolder has two sections:

```text
documentation/
  {topic}/
    general-best-practices/   — Industry reference (READ-ONLY, never modify)
    project-specific/          — This project's implementation (MUST stay in sync with code)
```

### Rules

1. **Never modify `general-best-practices/`.** These are reference benchmarks shipped with the project.
2. **Update `project-specific/` as part of every PR** that changes the topic area. If you add a pipeline, update the pipeline docs. If you change a data source, update the data docs. Documentation updates are not optional — the work is incomplete without them.
3. **Read best practices before implementing.** Before building something new, read the relevant `general-best-practices/` doc and compare your design against it. Note intentional deviations in `project-specific/`.
4. **Keep inventories current.** If a `project-specific/` doc has an inventory table (datasets, pipelines, notebooks, etc.), it must match the codebase. Update it before starting new work if it's stale.
5. **Document decisions, not just code.** Explain *why* an architectural choice was made. Include dates for significant decisions.

## Workflow

- Conventional commits: `fix:`, `feat:`, `refactor:`, `docs:`, `chore:`, `test:`
- Reproducibility first — every result must be regenerable from raw data + code
- Commit notebooks with cleared outputs unless they serve as reports
- When compacting context, preserve: data provenance, processing decisions, key results, data issues found
