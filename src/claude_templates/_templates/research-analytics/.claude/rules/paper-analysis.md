---
paths:
  - "**/data-analysis/**"
---

# Paper Analysis Rules

## Single Source of Truth

- Maintain **one notebook** that contains all tables and key figures referenced in the paper
- This notebook is the canonical reference — if a number appears in the paper, it must be traceable here
- Name it clearly: `00-paper-tables.ipynb` or similar
- Additional notebooks for exploratory analysis or supplementary figures are fine

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
- Save publication-quality figures to a `figures/` directory (PNG 300 DPI minimum)
- Save formatted tables to a `tables/` directory when needed for the paper

## Data Provenance

When discussing any result, the agent MUST:

1. **Name the source table** — Which Glue table or processed dataset is used
2. **Describe the pipeline** — How data flows from `data-source/` through `data-processing/` to this analysis
3. **Explain transformations** — What filters, joins, or aggregations were applied
4. **Define variables** — What each column means in business/research terms

Never present a number without explaining where it comes from.

## Paper Integration

- Structure analysis notebooks to mirror paper sections where practical
- Each figure/table should have a clear identifier matching the paper (e.g., "Table 1", "Figure 3")
- Include notes on what the result means for the paper's argument
- The goal is to reduce paper-writing time — the repo should contain everything needed to write any section

## Anti-Patterns — NEVER Do

1. **Unexplained results** — every number must be traceable to source data
2. **Code-heavy notebooks** — extract logic to `src/`, keep notebooks lean
3. **Missing figure labels** — axes, titles, and legends are mandatory
4. **Scattered tables** — paper tables belong in the source-of-truth notebook
5. **Print-based output** — use proper display methods for tables and figures
