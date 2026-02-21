---
name: write-paper-section
description: "Draft a paper section using data and analysis from the repository."
---

# Write Paper Section

Draft a section by pulling from the repository's data, processing, and analysis.

## Steps

### 1. Identify Relevant Tables and Figures

- Find which tables/figures from `data-analysis/` are relevant to this section
- Read the source-of-truth notebook to understand the results
- Note the table/figure identifiers

### 2. Trace Data Provenance

- For each table/figure, trace back through `data-processing/` to `data-source/`
- Document the full pipeline so the methodology description is accurate
- Note any assumptions, filters, or business rules applied

### 3. Write the Methodology

- Describe the data source (provider, coverage, time period)
- Explain the processing steps in plain language (no code references)
- Describe any variable construction or transformations
- Be precise about sample selection and exclusion criteria

### 4. Write the Results Narrative

- Describe what the tables/figures show
- Interpret the results — explain the patterns, not just the numbers
- Connect findings to the research question
- Use academic tone: precise, measured, evidence-based

### 5. Add Context and Caveats

- Note any limitations of the data or methodology
- Compare with existing literature where appropriate
- Suggest robustness checks if applicable

## Output

- Markdown text suitable for inclusion in a paper draft
- Academic tone throughout
- All claims backed by specific tables/figures from the repo
- No code references — describe the process, not the implementation
