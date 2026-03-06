# Economics Research Paper — Best Practices

## General Principles

- Every sentence must earn its place. If it does not advance the argument, cut it.
- Write for the referee — busy, skeptical, reading dozens of papers. Make their job easy.
- One paper, one idea. If the paper tries to answer more than one question, split it.
- The paper should be internally consistent: the introduction promises, the body delivers, the conclusion summarizes. No surprises, no orphaned claims.
- Never claim more than the data supports. Overstatement is the fastest route to a desk reject.
- Target 30-40 pages including tables and figures (30 for JDE-style field journals).

## Paper Structure

Standard structure for applied micro papers. Adapt when the paper's argument requires it — some papers merge sections, add institutional context, or reorder data and strategy.

1. **Title** — short, specific, informative. Pattern: "[Mechanism/Effect]: [Evidence Type] from [Setting]"
2. **Abstract** — 150 words max; question, method, main result **with a number**, mechanism, implication
3. **Introduction** — the most critical section (see framework below)
4. **Literature review** — 1-1.5 pages, organized by channel, ending with a gap paragraph
5. **Data** — one paragraph per source, summary statistics table, treatment definition
6. **Empirical strategy** — identifying assumption in plain language, estimating equation, pre-trends
7. **Results** — ATT + SE, economic magnitude, event-study figure
8. **Robustness** — alternative estimators, sample restrictions, placebo tests
9. **Heterogeneity** — predetermined splits, explicitly descriptive
10. **Mechanisms** — theoretical channels, distinguished from heterogeneity
11. **Conclusion** — 1-1.5 pages: finding, policy implication, limitations, future work
12. **References** — alphabetical, consistent, every citation matched

## Introduction Framework

The introduction is 60% of whether the paper gets read. Structure it paragraph by paragraph:

| Paragraph | Content |
|-----------|---------|
| **1** | The economic question + why it matters (open with the question, not background) |
| **2** | Setting and identifying variation (why this setting is well-suited) |
| **3** | Ex ante ambiguity (theoretical tension — why is the sign unclear?) |
| **4** | Data and identification (brief — one paragraph) |
| **5** | Results with numbers (point estimates + SE; this is where the referee decides) |
| **6** | Contributions (max 3, numbered, each referencing specific literature) |
| **7** | Roadmap (optional — if it adds nothing beyond section titles, delete it) |

**Do not:** open with a broad statement, announce what the paper does before explaining why it matters, duplicate the abstract, or leave contributions implicit.

## Reporting Conventions

- ATT followed by standard error: "The ATT is 18.6 percent (s.e. = 0.085)"
- **Never** report p-values in running text. Significance stars belong in tables only
- Point estimates in percent when using Poisson or log specifications
- Interpret economic magnitude: "an 18.6 percent increase in patenting" not "significant at the 5 percent level"
- Never: "statistically significant at the X percent level"

## Style Rules

- Declarative, precise, direct sentences. No hedging ("it seems," "it appears," "it could be argued")
- Active voice. "We estimate" not "It is estimated"
- No colons to introduce clauses or results in running prose. Restructure
- No em-dashes as punctuation. Use commas or separate sentences
- No informal connectives ("Interestingly," "Importantly," "It is worth noting that")
- No vague intensifiers ("very", "extremely", "highly")
- Never start with bare "This" — follow with the noun: "This evidence indicates" not "This indicates"
- Short paragraphs. Each opens with a topic sentence stating the main claim
- Do not open sections by announcing what they do ("This section investigates..."). Open with the substantive claim
- One idea per paragraph. No paragraph longer than half a page

## Tables and Figures

- Tables must be **self-explanatory**. Include: descriptive title, clear column headers, detailed notes (estimator, FE, clustering level, covariate definitions)
- Standard errors in parentheses. Stars defined in notes
- Event-study plots: confidence intervals, marked omitted period, labeled axes
- Number tables and figures consecutively. Refer to every one in the text — no orphaned exhibits
- Consistent formatting across all tables

## Literature Review Rules

- Organize by **channel or mechanism**, not paper by paper
- End with a **gap paragraph**: (a) what's known, (b) what's missing, (c) how this paper fills it
- The gap must mirror the contributions in the introduction
- 1-1.5 pages. A 5-page literature survey signals a working paper
- Never end with "this paper contributes to the growing literature on X"
- Do not use AI chat tools in chat mode to draft the lit review — they produce paper-by-paper catalogs, not integrated arguments

## Heterogeneity vs. Mechanisms

- **Heterogeneity** shows *who* responds. It is descriptive. Split on predetermined variables only
- **Mechanisms** show *why* the effect exists. State the hypothesis before the test
- These are separate sections. State explicitly that heterogeneity splits are descriptive
- Null mechanism results are informative — report them

## Research Question Quality Test

1. **"Why isn't the answer obvious?"** — Multiple outcomes must be plausible. You should never hope for a specific result.
2. **"Why should I care?"** — The answer must be consequential for economics broadly, not just one subfield.

If either test fails, the question is not ready.

## Workflow

- Write the results section first, then build data and identification to support it
- Write the introduction last (or rewrite it last) — it should promise exactly what the paper delivers
- Read published papers in your target journal to calibrate length, tone, and structure
- Have someone outside your field read the introduction — if they can't state the question, finding, and contribution, rewrite it
