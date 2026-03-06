# Economics Peer Review Documentation — Mandatory Maintenance

This project maintains structured documentation in `documentation/econ-peer-review/`. Keeping it current is **not optional** — it is part of every review and revision cycle.

## Folder Structure

```
documentation/econ-peer-review/
  general-best-practices/   — Reference methodology (READ-ONLY, never modify)
  project-specific/          — This project's review tracking (MUST stay in sync)
```

## Rules

### 1. Never modify `general-best-practices/`

These are reference documents for conducting and responding to peer reviews. Treat them as read-only benchmarks.

### 2. Read best practices before reviewing or revising

| Task | Read first |
|------|-----------|
| Write a referee report | `01-conducting-a-peer-review.md` — structure, timeline, recommendations |
| Evaluate identification | `02-evaluating-econometric-designs.md` — DiD, IV, RDD, Poisson checklists |
| Check tone before submitting | `03-tone-and-ethics.md` — constructive criticism, ethics |
| Systematic evaluation | `04-evaluation-checklists.md` — section-by-section checklists |

### 3. Track every referee comment

When you receive a referee report:
1. Create or update `project-specific/01-review-tracker.md` with every comment
2. Categorize as Major or Minor
3. Mark status: `[OPEN]`, `[IN PROGRESS]`, `[DONE]`
4. Never delete resolved items — keep the full history

### 4. Address comments in priority order

1. Identification and methodology (fatal if unresolved)
2. Missing analyses (robustness, heterogeneity, mechanisms)
3. Structural and narrative issues
4. Results presentation
5. Style and exposition
6. Typos and minor corrections
7. Citation coverage
