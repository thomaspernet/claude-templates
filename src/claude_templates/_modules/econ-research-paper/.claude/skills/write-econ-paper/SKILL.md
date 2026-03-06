---
name: write-econ-paper
description: "Use this skill when writing, structuring, or improving an empirical economics research paper. Invoke when the user mentions a research paper, thesis, working paper, introduction, literature review, empirical strategy, robustness checks, or JEL codes — even if they only say 'write the intro' or 'draft the results section'."
---

# Write Economics Research Paper

## When to Use

**Perfect for:**
- Writing or restructuring any section of an empirical economics paper
- Drafting a research proposal or thesis introduction
- Reviewing whether a paper follows standard economics conventions
- Building the WHAT/WHY/HOW framework for an introduction

**Not ideal for:**
- Theoretical or purely mathematical economics papers
- Literature surveys with no empirical contribution
- Writing a single table note or formatting fix (edit directly)

---

> **Core Philosophy:** A good economics paper answers a question whose answer is not obvious, whose answer is consequential, and whose empirical strategy convincingly addresses endogeneity. Structure and clarity are not cosmetic — they determine whether the paper gets read past the first page.

## CRITICAL

1. **Every introduction must answer WHAT/WHY/HOW.** WHAT 1 (research question), WHY 1 (consequential), WHY 2 (not obvious), WHAT 2 (contribution), HOW 1 (data), HOW 2 (empirical strategy), WHAT 3 (findings). Missing any of these makes the introduction incomplete.
2. **Economic magnitude over statistical significance.** Never report a result as "significant" without discussing its real-world magnitude. In large datasets, trivially small effects are statistically significant.
3. **Tables must stand alone.** A reader must understand a table without reading the text, and vice versa. Every table needs clear headers, variable definitions, sample descriptions, and notes.

---

## Step 1: Define the Research Question

Before writing anything, verify the question passes both tests:

- **"Why isn't the answer obvious?"**
  - If estimating impact of A on B: identify endogeneity problems (reverse causality, omitted variables, selection bias)
  - If testing a theory: present competing theories that predict opposite signs
- **"Why should I care?"**
  - What policy recommendations would follow from each possible answer?
  - Would a non-economist understand why this matters?

If either test fails, refine the question before proceeding.

## Step 2: Write the Title Page

1. **Title** — Present the research question in an eye-catching way. Good titles often use a question or a surprising juxtaposition.
2. **Abstract** — 100-150 words. Write AFTER the conclusion and introduction. Communicate the main result in a way that convinces readers to continue.
3. **Keywords** — No more than 2 lines.
4. **JEL codes** — Use the AEA classification system. Include codes for the methodology (e.g., C36 for IV) and the field (e.g., I21 for education).

## Step 3: Write the Introduction (Most Important Section)

Structure the introduction to answer all seven questions:

1. **Contextualization** (1 paragraph) — Real-world context with statistics, examples, or anecdotes. Ground the paper in reality.
2. **WHAT 1** — State the objective of the paper.
3. **WHY 1** — Explain why the answer is consequential.
4. **WHY 2** — Explain why the answer is not obvious (endogeneity, heterogeneity, competing theories).
5. **WHAT 2** — State the contribution to the literature.
6. **HOW 1** — Present the data.
7. **HOW 2** — Present the empirical strategy and why it solves endogeneity.
8. **WHAT 3** — Present the results (include economic magnitude).
9. **Roadmap** — Final paragraph outlining the paper's structure.

Upper limit: 5 pages. A non-specialist should understand every point.

## Step 4: Write the Related Literature

- Decompose into max 3 strands.
- Only cite papers closely linked to your question.
- Use your own words — no copy-pasted abstracts.
- Frame positively: "We complement these approaches in several ways. First..."
- Never say: "The deficiency of X's approach" or "These papers suffer from."
- You may elaborate on WHY 2 here (why the answer is not obvious).

## Step 5: Write the Data Section

- One subsection per set of variables: dependent variable, explanatory variable, instrument (if applicable), controls.
- Justify data source choice when alternatives exist.
- Include descriptive statistics table: N, mean, SD, min, max.
- Comment on the descriptive statistics — don't just present the table.

## Step 6: Write the Empirical Strategy

- Describe the strategy in detail.
- Convince the reader it solves endogeneity problems.
- If using IV: explain why the instrument is valid (affects Y only through X).
- Use visual arguments: scatterplots of instrument vs. endogenous variable.
- Write regression equations clearly with precise variable definitions.

## Step 7: Write the Results

- Present regression tables that are **self-explanatory**.
- Derive main results clearly from the tables.
- Focus on economic magnitude, not just stars.
- Put magnitude in perspective (e.g., "equivalent to X% of a standard deviation" or "comparable to the effect of Y").

## Step 8: Write Robustness Checks

- First priority: identify alternative stories (competing channels) and show findings survive.
- Second priority: sensitivity to alternative measures of dependent variable, explanatory variable, instrument.
- Test sensitivity to outlier removal.
- Present in tables with the same format as main results.

## Step 9: Write the Conclusion

- Max 3 pages.
- Summarize the contribution.
- Emphasize policy implications.
- Point to avenues for future research (opportunity to acknowledge limitations without being overly negative).

## Step 10: Final Polish

- Check all references are complete, alphabetical, consistently formatted.
- Verify every number in the text matches the tables.
- Remove all intensifiers ("very", "extremely", "highly").
- Ensure each paragraph contains one idea and is shorter than half a page.
- Re-read the introduction — does it answer all 7 questions?

## Output

Deliver the section in academic prose, ready for inclusion in the paper:

```markdown
## {Section Title}

{Content following the conventions above}
```

When delivering a full paper structure, provide the outline:

```
1. Title page
   - Title: {title}
   - Abstract: {100-150 words}
   - Keywords: {keywords}
   - JEL: {codes with descriptions}

2. Introduction
   - Contextualization: {topic}
   - WHAT 1: {research question}
   - WHY 1: {why consequential}
   - WHY 2: {why not obvious}
   - WHAT 2: {contribution}
   - HOW 1: {data}
   - HOW 2: {empirical strategy}
   - WHAT 3: {key findings}

3. Related Literature ({n} strands)
4. Data ({n} variable sets)
5. Empirical Strategy
6. Results
7. Robustness Checks
8. Conclusion
9. References
```

## Checklist

- [ ] Research question passes "Why not obvious?" and "Why should I care?" tests
- [ ] Introduction answers all 7 questions (WHAT 1-3, WHY 1-2, HOW 1-2)
- [ ] Introduction starts with real-world contextualization
- [ ] Introduction ends with roadmap
- [ ] Introduction is under 5 pages
- [ ] Literature review uses max 3 strands, no negative framing
- [ ] Data section has one subsection per variable set with descriptive statistics
- [ ] Empirical strategy explicitly addresses endogeneity
- [ ] Tables are self-explanatory (standalone from text)
- [ ] Results discuss economic magnitude, not just statistical significance
- [ ] Robustness checks address alternative stories first
- [ ] Conclusion is under 3 pages with policy implications
- [ ] References are alphabetical and consistently formatted
- [ ] Paper is under 40 pages total
- [ ] No vague intensifiers, all sentences have subject-verb-object
