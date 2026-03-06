# Economics Peer Review — Best Practices

## Purpose of a Peer Review

A peer review serves three audiences:

1. **The editor** — needs a clear recommendation and concise summary of strengths/weaknesses
2. **The authors** — need specific, actionable feedback to improve the paper
3. **The field** — benefits when the review raises the quality bar without gatekeeping

A good review is honest, constructive, and precise. It identifies problems and suggests how to fix them.

## Review Structure (Mandatory)

Every review must contain these sections, in order:

1. **Summary** (1 paragraph) — question, method, finding, contribution in your own words. No evaluation here.
2. **Overall assessment** (1-2 paragraphs) — main strength, main weakness, direct judgment on publishability.
3. **Major issues** (3-5 max) — problems that prevent publication. Each: what, why it matters, how to fix.
4. **Minor issues** — problems that should be fixed but don't threaten the core contribution.
5. **Detailed comments** (optional) — page/section/table-level notes for revision.
6. **Recommendation** — Accept / Major R&R / Minor R&R / Reject.

## Reporting Conventions

- Be specific with numbers: "The pre-trend at t=-3 is -0.184 (s.e. = 0.149), large relative to the ATT of 0.145" — not "the pre-trends are concerning."
- Criticize the paper, not the authors: "The strategy does not account for X" not "The authors fail to consider X."
- If uncertain whether a concern is fatal, say so: "I am uncertain whether this threatens the main result, but the authors should address it."
- Suggest fixes, not just problems.

## What Constitutes a Major Issue

| Category | Examples |
|----------|---------|
| Identification | Endogeneity, parallel trends violation, SUTVA, bad instruments |
| Sample/data | Selection bias, survivorship, measurement error, inadequate N |
| Specification | Wrong estimator, omitted variables, post-treatment controls |
| Interpretation | Results don't support claims, alternative explanations not ruled out |
| Missing analysis | No robustness, no heterogeneity, mechanisms asserted not tested |

## Tone Rules

- Criticize the paper, not the authors
- Suggest fixes, not just problems
- Do not inflate minor issues to justify a negative recommendation
- Do not bury identification problems in minor comments
- Never demand citations to your own work (unless genuinely relevant)
- Never ask the authors to write a different paper
- Never reject because results are null or unexpected
- Never be dismissive, condescending, or personally critical
- Never request analyses that are infeasible given the data

## AI-Assisted Review Rules

- AI can check internal consistency, flag missing tests, identify style issues
- AI **cannot** judge identification credibility, assess novelty, or make editorial recommendations
- Always provide AI with the full paper, not sections in isolation
- Treat AI output as a first draft — verify every claim against the paper
- Write the overall assessment and recommendation yourself

## Review Timeline

- First read (1-2h): cover to cover, no notes, form general impression
- Second read (2-3h): mark issues, check numbers, note identification concerns
- Writing (1-2h): organize into the structure above
- Cooling period (1 day): re-read before submitting to check tone

## Tracking Review Issues During Revision

When revising your own paper in response to a referee report:

- Maintain a single file listing every comment with status: `[OPEN]`, `[IN PROGRESS]`, `[DONE]`
- Do not delete resolved items — keep the full history
- Address every comment in the response letter, even to respectfully disagree
- Priority order: identification → missing analyses → structure → presentation → style → typos → citations
