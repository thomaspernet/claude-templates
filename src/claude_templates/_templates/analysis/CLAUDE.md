# {PROJECT_NAME}

## BUGS.md and MISTAKES.md

Read both files at the start of every session. If you encounter a bug or make a mistake, update the relevant file before continuing.

## Project & Tech

- Python with pandas, polars, matplotlib, seaborn, plotly, scikit-learn
- Jupyter notebooks for exploration and presentation
- `uv` for dependency management
- Data formats: CSV, Parquet, JSON

## Architecture

```
notebooks/          — exploration and presentation notebooks
src/                — reusable functions and modules
data/
  raw/              — original, immutable data files
  processed/        — cleaned and transformed data
  output/           — final datasets for delivery
reports/
  figures/          — saved charts and visualizations
  tables/           — exported summary tables
```

## Critical Rules

- **Never modify raw data files.** `data/raw/` is read-only.
- All transformations must be reproducible from raw data.
- Pin random seeds for any stochastic operations (`random_state=42`).
- Always specify `dtype` when reading data files.
- Document assumptions inline where they affect logic.
- Extract reusable logic into `src/` functions — notebooks are for orchestration, not library code.

## Code Style

- Type hints on all functions in `src/`.
- Docstrings with parameter descriptions on all public functions.
- `snake_case` everywhere (variables, functions, files).
- Notebooks: markdown cells explain the **why**, code cells do the **what**.
- Keep notebook cells short — one logical step per cell.
- **Prefer clarity and readability** over cleverness in all code
- Organize modules into **folders and subfolders** by domain — avoid many files under the same directory

## Dev Commands

```bash
uv run pytest              # run tests for src/ modules
uv run jupyter lab         # launch notebook environment
uv run ruff check          # lint Python files
```

## Testing

- `pytest` for all functions in `src/`.
- Notebooks validated by executing top-to-bottom with `jupyter nbconvert --execute`.
- Test edge cases: empty DataFrames, NaN values, type mismatches.

## Workflow

- Conventional commits: `fix:`, `feat:`, `refactor:`, `docs:`, `chore:`, `test:`
- Reproducibility first — every result must be regenerable from raw data + code.
- Commit notebooks with cleared outputs unless they serve as reports.
