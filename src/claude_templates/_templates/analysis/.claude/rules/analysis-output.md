---
paths:
  - "**/data-analysis/**"
---

# Analysis Output Rules

## Single Source of Truth

- Maintain **one notebook** that contains all key results (tables and figures)
- This notebook is the canonical reference for final outputs
- Name it clearly: `00-main-results.ipynb` or similar
- Additional notebooks for exploratory analysis or individual deep-dives are fine

## Notebook Style

- Markdown cells explain **intent and interpretation**, never implementation
- Interpret results in narrative form — do not restate what the code output shows
- Short paragraphs, direct language, academic tone
- Every code cell must be preceded by a markdown cell explaining **why** this step matters
- Use `%load_ext autoreload` / `%autoreload 2` at the top of every notebook

## Display & Output

- Prefer **tables and figures** over raw `print()` statements
- Use `DataFrame.style`, `tabulate`, or rich display for tabular data
- Label all axes, add titles, use consistent color palettes
- Use colorblind-safe palettes: `viridis`, `cividis`, or seaborn `colorblind`
- Save publication-quality figures (PNG 300 DPI, SVG for web)
- Always `plt.tight_layout()` or `bbox_inches='tight'` before saving

## Data Provenance

When discussing any result, the agent MUST:

1. **Name the source data** — Which raw or processed dataset is used
2. **Describe the pipeline** — How data flows from `data-source/` through `data-processing/` to this analysis
3. **Explain transformations** — What filters, joins, or aggregations were applied
4. **Define variables** — What each column means in domain terms

Never present a number without explaining where it comes from.

## Anti-Patterns — NEVER Do

1. **Unexplained results** — every number must be traceable to source data
2. **Code-heavy notebooks** — extract logic to `src/`, keep notebooks lean
3. **Missing figure labels** — axes, titles, and legends are mandatory
4. **Print-based output** — use proper display methods for tables and figures
5. **Charts without source annotation** — always note where the data comes from
