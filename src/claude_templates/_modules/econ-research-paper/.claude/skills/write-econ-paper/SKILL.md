---
name: write-econ-paper
description: "Use this skill when writing, structuring, or improving an empirical economics research paper. Invoke when the user mentions a research paper, thesis, working paper, introduction, literature review, empirical strategy, robustness checks, heterogeneity, mechanisms, or JEL codes — even if they only say 'write the intro' or 'draft the results section'."
---

# Write Economics Research Paper

## When to Use

**Perfect for:**
- Writing or restructuring any section of an empirical economics paper
- Drafting a research proposal or thesis introduction
- Reviewing whether a paper follows top-tier journal conventions (AER, QJE, JDE, JIE, RESTUD)
- Building the introduction framework for an applied micro paper

**Not ideal for:**
- Theoretical or purely mathematical economics papers
- Literature surveys with no empirical contribution
- Writing a single table note or formatting fix (edit directly)

---

> **Core Philosophy:** One paper, one idea. Every sentence must earn its place. Write for the referee — busy, skeptical, reading dozens of papers. The introduction is 60% of whether the paper gets read. Never claim more than the data supports.

## CRITICAL

1. **The introduction must open with the question, not background.** State what the paper does in the first or second sentence. Do not open with broad context ("Climate change is one of the greatest challenges..."). Lead with the economic question and why it matters.
2. **Report economic magnitude, never just significance.** "An 18.6 percent increase in patenting" is informative; "significant at the 5 percent level" is not. Never report p-values in running text — significance stars belong in tables only. Use ATT followed by standard error: "The ATT is 18.6 percent (s.e. = 0.085)."
3. **Heterogeneity is not mechanisms.** Heterogeneity shows *who* responds (descriptive). Mechanisms show *why* the effect exists (the theoretical channel). These are separate sections. State explicitly: "These splits are descriptive and identify correlates of the response, not causal mechanisms."

---

**Note on flexibility:** The structure below is a guide for applied micro papers targeting top journals. Some papers need to deviate — theory-heavy papers may merge the empirical strategy into the model section, development papers may need longer institutional context, etc. Adapt the structure to serve the paper's argument, not the other way around.

---

## Step 1: Define the Research Question

Before writing anything, verify the question passes both tests:

- **"Why isn't the answer obvious?"** — Multiple outcomes must be plausible. If you're hoping for a specific result, the question isn't interesting.
- **"Why should I care?"** — The answer must be consequential for economics, not just for the specific field.

One paper, one question. If you're trying to answer more than one, split it.

## Step 2: Title and Abstract

**Title:** Short, specific, informative. The reader should know the topic, setting, and type of evidence from the title alone.
- Good pattern: "[Mechanism/Effect]: [Evidence Type] from [Setting]"
- Avoid question marks, puns, and vague framing ("Essays on...", "Towards a...")

**Abstract:** 150 words maximum (some journals allow 200).
1. Question
2. Setting and method in one sentence
3. Main result **with a number** (point estimate + SE)
4. Mechanism or heterogeneity
5. Implication

No citations. No filler ("This paper contributes to the literature..."). Start with what the paper does.

## Step 3: Write the Introduction

The introduction is 60% of whether the paper gets read. Structure it paragraph by paragraph:

| Paragraph | Content |
|-----------|---------|
| **1. Question + why it matters** | Open with the economic question. State what the paper does. Convey why this matters for economics broadly. |
| **2. Setting and context** | Why this setting is well-suited. Describe the identifying variation informally but precisely. |
| **3. Ex ante ambiguity** | Theoretical tension — why is the sign unclear? Signals the paper isn't confirming a foregone conclusion. |
| **4. Data and identification** | One paragraph: dataset, key variables, estimation strategy. Enough for the referee to assess credibility. |
| **5. Results** | Main findings **with numbers** (point estimates + SE). Heterogeneity and mechanisms briefly. This is where the referee decides if the paper is interesting. |
| **6. Contributions** | Three maximum, numbered. Each references the specific literature it advances. Be precise: "first firm-level causal estimate of X" > "contributes to the literature on X." |
| **7. Roadmap** (optional) | If included, make it substantive. "Section 2 establishes the aggregate patenting response" > "Section 2 reviews the literature." If it adds nothing beyond section titles, delete it. |

**Pitfalls:**
- Do not open with a broad statement about the state of the world
- Do not announce what the paper does before explaining why it matters
- Do not duplicate the abstract
- Do not leave contributions implicit — the referee uses this paragraph to evaluate novelty

Upper limit: 5 pages. A non-specialist should understand every point.

## Step 4: Literature Review

**Length:** 1-1.5 pages for top journals (AER/QJE fold it into the intro). A 5-page lit review signals a working paper, not a journal submission.

**Structure by channel/mechanism, not paper by paper:**
- Bad: "Smith (2020) finds X. Jones (2021) finds Y."
- Good: "Three mechanisms link disasters to innovation. On the disruptive side, [citations]. On the adaptive side, [citations]."

**The gap paragraph (mandatory):** End with: (a) what prior work established, (b) what remains unknown, (c) how this paper fills the gap. The gap statement must mirror the contributions in the introduction.

**What to cut:** Macro cross-country evidence irrelevant to your identification. Papers already discussed in the intro. Papers topically related but methodologically distant.

**Do not use AI chat tools to draft the lit review.** They produce paper-by-paper catalogs, not integrated arguments. The lit review must be written with the full paper in mind so every citation connects to your identification and contribution.

## Step 5: Data

- One paragraph per data source: provider, coverage (years, geography, unit), key variables
- Explain merging procedures and identifiers for reproducibility
- Report sample restrictions with justification for each dropped observation
- Summary statistics table: means, SD, min, median, max — paneled by variable type
- Discuss summary statistics in text — flag unusual patterns (skewness, zeros, outliers)
- Define the treatment variable precisely. If constructed (geocoding, matching, thresholds), explain step by step
- Report treated vs. control counts and how treatment varies over time

## Step 6: Empirical Strategy

- State the identifying assumption **in plain language** before writing equations
- Explain why the assumption is credible in this specific setting
- Present the estimating equation with every term defined
- Justify the estimator choice. If using staggered DiD, acknowledge the TWFE bias literature and cite the methodological papers
- Specify clustering level and justify it
- For DiD: show event-study plot with pre-treatment coefficients. Report the coefficients and SEs explicitly — don't just say "no evidence of pre-trends"
- Report the preferred specification without controls as the benchmark. Add controls as robustness to assess stability
- If controls are post-treatment, acknowledge this explicitly

## Step 7: Results

- Lead with the main estimate. Report ATT with standard error in parentheses
- Never report p-values in running text. Stars belong in tables only
- Interpret economic magnitude: "An 18.6 percent increase in patenting" not "significant at the 5 percent level"
- Show the event-study figure alongside the table
- Point estimates in percent when using Poisson or log specifications

## Step 8: Robustness

- Alternative estimators (stacked DiD, alternative clustering, Conley SEs)
- Sensitivity to sample restrictions (dropping outliers, varying treatment definitions)
- Placebo tests if applicable
- Do not oversell. If an alternative specification gives different results, discuss honestly

## Step 9: Heterogeneity

- Split on **predetermined** variables (measured before treatment). Never split on post-treatment outcomes
- State explicitly: "These splits are descriptive and identify correlates of the response, not causal mechanisms"
- Report ATTs for each subgroup with standard errors
- Discuss the economic logic for each split before showing results
- Connect to the mechanisms section that follows

## Step 10: Mechanisms

- Mechanisms show **why** the effect exists — the theoretical channel
- State the hypothesis before the test
- Explain how you operationalize (proxy variable, sample split, interaction)
- Report results and interpret in terms of the theoretical channel
- Discuss which mechanisms do *not* work — null results are informative

## Step 11: Conclusion

- **1-1.5 pages maximum.** Shorter is better — this should be the shortest section.
1. Restate the main finding in one sentence
2. Summarize the key heterogeneity/mechanism result
3. Policy implication (one paragraph, concrete)
4. Limitations honestly (sample, identification, external validity)
5. Future work briefly (one or two sentences, not a research agenda)

Do not repeat the introduction verbatim. Do not overclaim external validity. Do not introduce new results.

## Step 12: Final Polish

- Every number in text matches the tables
- All references complete, alphabetical, consistent style
- Every citation in text appears in references and vice versa
- Compile and proofread the PDF — broken cross-references signal carelessness
- Have someone outside your field read the introduction. If they cannot state the question, finding, and contribution, rewrite it
- Write the introduction last (or rewrite it last) — it should promise exactly what the paper delivers

## Output

Deliver the section in academic prose, ready for inclusion:

```markdown
## {Section Title}

{Content following the conventions above}
```

When delivering a full paper outline:

```
1. Title: {title}
   Abstract: {150 words with headline estimate}
   Keywords / JEL: {codes}

2. Introduction
   P1: Question + why it matters
   P2: Setting and identifying variation
   P3: Ex ante ambiguity
   P4: Data and identification (brief)
   P5: Results with numbers
   P6: Contributions (max 3, numbered)
   P7: Roadmap (optional, substantive)

3. Literature ({n} strands, organized by channel)
   Gap paragraph: {what's known} → {what's missing} → {how this paper fills it}

4. Data ({n} sources)
   Summary statistics table
   Treatment definition and variation

5. Empirical Strategy
   Identifying assumption (plain language)
   Estimating equation
   Pre-trends / event study

6. Results
   Main estimate: ATT = {X}% (s.e. = {Y})
   Event-study figure

7. Robustness
8. Heterogeneity (descriptive, predetermined splits)
9. Mechanisms (theoretical channels)
10. Conclusion (1-1.5 pages)
11. References
```

## Checklist

### Structure
- [ ] One paper, one question — not trying to answer multiple things
- [ ] Research question passes "Why not obvious?" and "Why should I care?"
- [ ] Title is short, specific, informative (no puns or question marks)
- [ ] Abstract under 150 words with headline estimate and SE
- [ ] Introduction opens with the question, not broad context
- [ ] Introduction reports results with numbers (point estimates + SE)
- [ ] Contributions are numbered, precise, and reference specific literatures
- [ ] Lit review organized by channel, not paper by paper
- [ ] Lit review ends with a gap paragraph mirroring the contributions
- [ ] Data section justifies every sample restriction
- [ ] Empirical strategy states identifying assumption in plain language
- [ ] Event-study / pre-trends reported with coefficients and SEs
- [ ] Results lead with ATT + SE, no p-values in running text
- [ ] Economic magnitude interpreted, not just statistical significance
- [ ] Tables are self-explanatory with full notes
- [ ] Heterogeneity clearly labeled as descriptive, splits on predetermined variables
- [ ] Mechanisms distinguished from heterogeneity with theoretical hypotheses
- [ ] Conclusion under 1.5 pages, no new results, no overclaiming
- [ ] Paper under 40 pages total (30 for JDE-style journals)

### Prose quality (AI-specific failure modes)
- [ ] No patronizing transitions ("For pricing, this means...", "The implication is...", "Practitioners should be aware...")
- [ ] No editorializing ("most important number", "most consequential finding", "confirms the intuition")
- [ ] No student-level anthropomorphizing ("the coefficients tell a story", "makes economic sense")
- [ ] No straw-man caveats ("This does not mean X" where nobody claimed X)
- [ ] No defensive methodology justification (why OLS not ML, why classical not neural)
- [ ] No marketing language ("designed to improve", "positioned to support", "value proposition")
- [ ] No vague adjectives without numbers ("modest", "meaningful", "substantial", "reassuring")
- [ ] No repeated "(coefficient = X, s.e. = Y)" syntax in running text — state economic meaning, cite the table
- [ ] No fabricated client positions or assumed preferences not provided by the client
- [ ] No rhetorical questions opening sections
- [ ] All equation subscripts formally defined
- [ ] No hedging, no intensifiers, no informal connectives, active voice
