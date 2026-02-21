# Notebook Best Practices

## Markdown Cells

- Explain **intent**, not implementation — describe what the analysis accomplishes, not what the code does
- Interpret results in narrative form — never restate code output
- Short paragraphs, direct language, academic tone
- One idea per cell — if a markdown cell covers two topics, split it

## Code Organization

- **Extract reusable logic into external modules** — notebooks are for orchestration and narrative, not library code
- Create functions/classes in `src/` or a dedicated package, import them into the notebook
- Keep code cells short and focused — one logical step per cell
- Use folders and subfolders to organize extracted modules by domain

## Autoreload Setup

Always include at the top of every notebook:

```python
%load_ext autoreload
%autoreload 2
```

This ensures changes to external modules are picked up automatically without restarting the kernel.

## Display & Output

- Prefer **tables and figures** over raw `print()` statements
- Use `DataFrame.style`, `tabulate`, or rich display for tabular data
- Save publication-quality figures to `reports/figures/`
- Label axes, add titles, use consistent color palettes
- Use `display()` explicitly when showing multiple outputs per cell

## Notebook as Document

- Treat every notebook as an **exportable document** — it should read coherently top-to-bottom
- Clear outputs before committing unless the notebook serves as a report
- Number notebooks for ordering: `01-data-loading.ipynb`, `02-cleaning.ipynb`
- Each notebook should have a clear purpose stated in the first markdown cell

## Anti-Patterns — NEVER Do

1. **Long code blocks in notebooks** — extract to modules, import and call
2. **Print-based debugging left in** — remove or convert to proper logging
3. **Undocumented cells** — every code cell should be preceded by a markdown cell explaining why
4. **Circular imports with src/** — keep module dependencies clean and one-directional
5. **Hardcoded file paths** — use `pathlib.Path` relative to project root or config
6. **Missing autoreload** — always load the extension at the top
