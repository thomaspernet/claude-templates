# Run Notebook

Execute a Jupyter notebook top-to-bottom and validate clean output.

## Steps

1. **Identify notebook** — Ask which notebook to run, or run all in `notebooks/`.
2. **Execute** — Run via:
   ```bash
   uv run jupyter nbconvert --to notebook --execute --inplace {notebook.ipynb}
   ```
3. **Check for errors** — If execution fails, report the cell number and error message.
4. **Validate output** — Confirm all cells produced expected output (no empty outputs where data is expected).
5. **Report** — Summary of execution: total cells, execution time, any warnings or errors.
