# Explain Table Provenance

Trace a table or figure back to its data source. Provide a complete provenance chain.

## Steps

1. **Identify the target** — Find the specified table or figure in `data-analysis/` notebooks
2. **Trace the data source** — Identify which processed datasets feed into it
3. **Walk the processing chain** — For each input, find the corresponding notebook/script in `data-processing/` that creates it
4. **Find the raw source** — Trace back to `data-source/` to identify the original provider and download method
5. **Document transformations** — At each step, explain: what data comes in, what transformations are applied, what comes out
6. **Summarize** — Produce a clear provenance chain from external source to final table/figure

## Output Format

```
## {Table/Figure Name}

### Provenance Chain

**Raw Source** → `data-source/{script}`
  - Provider: {name}
  - Data: {description}

**Processing** → `data-processing/{notebook}`
  - Input: {raw datasets}
  - Transformations: {description of joins, filters, aggregations}
  - Output: {processed dataset}

**Analysis** → `data-analysis/{notebook}`
  - Input: {processed dataset}
  - Final transformations: {any analysis-specific filters or calculations}
  - Output: {table/figure as displayed}

### Variable Definitions
- {column}: {definition}
```
