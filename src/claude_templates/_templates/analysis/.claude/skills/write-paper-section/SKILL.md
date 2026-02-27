---
name: write-paper-section
description: "Draft a paper section grounded in tables and figures from the repository."
---

# Write Paper Section

## When to Use

**Perfect for:**
- Writing or updating a Methods or Results section
- Drafting a section where all supporting evidence exists in the repo
- Ensuring methodology descriptions match the actual processing code

**Not ideal for:**
- Introduction or literature review sections (no repo data to trace)
- Sections with claims that can't be traced to a specific table or figure
- Sections requiring external citations not already in the analysis pipeline

---

> **Core Philosophy:** Methodology describes the process, not the code. Results describe patterns and meaning, not numbers in isolation. Every claim must be traceable to a specific artifact in this repository.

## ⚠️ CRITICAL

1. **Every claim must cite a specific table or figure from the repo.** No claims from memory, general knowledge, or assumptions. If a finding can't be traced to `data-analysis/`, it doesn't belong in this draft.
2. **Never reference code.** Describe the data flow and transformation logic in plain language. A reader should understand the methodology without seeing a single line of Python.

---

## Step 1: Identify Relevant Tables and Figures

- Find which tables/figures from `data-analysis/` are relevant to this section
- Read the source-of-truth notebook to understand the results
- Note the table/figure identifiers

## Step 2: Trace Data Provenance

- For each table/figure, trace back through `data-processing/` to `data-source/`
- Document the full pipeline so the methodology description is accurate
- Note any assumptions, filters, or business rules applied

## Step 3: Write the Methodology

- Describe the data source (provider, coverage, time period)
- Explain the processing steps in plain language (no code references)
- Describe any variable construction or transformations
- Be precise about sample selection and exclusion criteria

## Step 4: Write the Results Narrative

- Describe what the tables/figures show
- Interpret the results — explain the patterns, not just the numbers
- Connect findings to the research question
- Use academic tone: precise, measured, evidence-based

## Step 5: Add Context and Caveats

- Note any limitations of the data or methodology
- Compare with existing literature where appropriate
- Suggest robustness checks if applicable

## Output

Markdown text ready for direct inclusion in a paper draft:

```markdown
## {Section Title}

### Data and Methodology
[Plain-language description of data source, processing, variable construction]

### Results
[Pattern interpretation — what Table X / Figure Y shows and what it means]

### Limitations
[Data or methodology limitations relevant to this section]
```

All claims cite specific tables/figures: "(Table 1)", "(Figure 3)". No code references anywhere.
