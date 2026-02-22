# {PROJECT_NAME}

## Project & Tech

- **Notes**: Markdown
- **Citations**: BibTeX (`references.bib`)
- **Scripts**: Python (optional, for data collection or processing)
- **Web search**: For finding and evaluating sources

## Architecture

```
sources/            Raw materials (PDFs, saved pages, URLs)
notes/              Per-source notes (one file per source)
synthesis/          Cross-source analysis and themes
output/             Final documents (papers, reports, briefs)
references.bib      BibTeX bibliography
```

## Critical Rules

1. **Always cite sources** — Author, Year, URL. No uncited claims.
2. **Distinguish facts from interpretation** — Mark clearly what is reported vs. your analysis.
3. **Date-stamp all web sources** — URLs change. Record access date.
4. **Never present summaries as original analysis** — Paraphrasing is not analysis.
5. **Triangulate claims** — Minimum 2 independent sources for key findings.
6. **Mark confidence levels** — `[established]`, `[likely]`, `[speculative]` for claims.

## Note Format

Each file in `notes/` should follow:

```markdown
# {Source Title}

- **Author(s)**: ...
- **Year**: ...
- **URL/DOI**: ...
- **Accessed**: YYYY-MM-DD
- **Type**: journal article | book | report | web page | ...

## Key Points
- ...

## Relevant Quotes
> "..." (p. XX)

## My Analysis
- ...
```

## Writing Style

- Markdown with consistent ATX headings (# H1, ## H2, ### H3 max)
- One idea per paragraph
- Active voice preferred
- Reference-style links for URLs
- One sentence per line (diff-friendly)
- **Prefer clarity and readability** — direct language, no unnecessary jargon
- Organize files into **folders and subfolders** by topic — avoid many files under the same directory

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
2. **Update `project-specific/` as part of every PR** that changes the topic area. If you add a new research method, update the methodology docs. Documentation updates are not optional — the work is incomplete without them.
3. **Read best practices before implementing.** Before building something new, read the relevant `general-best-practices/` doc and compare your design against it. Note intentional deviations in `project-specific/`.
4. **Keep inventories current.** If a `project-specific/` doc has an inventory table (sources, methods, themes, etc.), it must match the codebase. Update it before starting new work if it's stale.
5. **Document decisions, not just code.** Explain *why* a methodological choice was made. Include dates for significant decisions.

## Workflow

- Define research question → search → evaluate sources → take notes → synthesize → write
- Commit prefixes: `docs:`, `feat:`, `refactor:`, `chore:`
- When compacting context, preserve: research questions, sources found, synthesis progress, open questions
