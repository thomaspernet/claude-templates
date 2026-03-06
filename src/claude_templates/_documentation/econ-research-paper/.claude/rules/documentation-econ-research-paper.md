# Economics Research Paper Documentation — Mandatory Maintenance

This project maintains structured documentation in `documentation/econ-research-paper/`. Keeping it current is **not optional** — it is part of every draft, revision, and data update.

## Folder Structure

```
documentation/econ-research-paper/
  general-best-practices/   — Reference methodology (READ-ONLY, never modify)
  project-specific/          — This project's research design (MUST stay in sync with paper)
```

## Rules

### 1. Never modify `general-best-practices/`

These are reference documents distilled from established research methodology courses. Treat them as read-only benchmarks. If you deviate from a practice, document the deviation in `project-specific/`, do not edit the original.

### 2. Documentation updates are mandatory

Every change to the paper must include corresponding documentation updates. This applies to:

- Changing the research question or contribution framing
- Adding, removing, or redefining variables
- Changing the identification strategy or instruments
- Receiving and responding to reviewer/advisor feedback
- Updating results or robustness checks

### 3. Read best practices before drafting

Before writing any section, read the relevant doc in `general-best-practices/`:

| Task | Read first |
|------|-----------|
| Define research question | `01-defining-a-research-project.md` — skeptic tests, contribution, feasibility |
| Write any section | `02-writing-a-research-paper.md` — structure, WHAT/WHY/HOW, writing tips |
| Design empirical strategy | `03-identification-and-empirical-strategy.md` — IV, DiD, RD, pitfalls |
| Create tables/figures | `04-tables-figures-and-presentation.md` — self-explanatory principle, magnitude |

### 4. Keep the research design current

The research design in `project-specific/01-research-design.md` is the source of truth for the WHAT/WHY/HOW framework. Before writing or revising any section:

1. Check if the research design matches the current state of the paper
2. If it doesn't, update it first
3. Then proceed with the writing

### 5. What to document

| Change | Update |
|--------|--------|
| Research question refined | `01-research-design.md` — WHAT/WHY/HOW table, decision log |
| Data source changed | `02-data-and-variables.md` (create if needed) — source, variables, sample |
| Strategy changed | `03-empirical-strategy.md` (create if needed) — identification, threats |
| Section drafted | `04-paper-outline.md` (create if needed) — outline with key arguments |
| Feedback received | `05-revision-log.md` (create if needed) — comment, response, action |
