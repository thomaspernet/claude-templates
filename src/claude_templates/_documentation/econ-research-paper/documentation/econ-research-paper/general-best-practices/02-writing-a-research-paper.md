# Writing a Good Economics Research Paper

> Sources: Valfort (2014), Pantheon-Sorbonne; conventions from AER, QJE, JDE, JIE, RESTUD, Econometrica.

## General Principles

- Every sentence must earn its place. If it does not advance the argument, cut it.
- Write for the referee — busy, skeptical, reading dozens of papers. Make their job easy.
- One paper, one idea. If the paper tries to answer more than one question, split it.
- The paper should be readable in one sitting. Target 30-40 pages including tables (30 for JDE-style field journals).
- The entire paper must be internally consistent: the introduction promises, the body delivers, the conclusion summarizes.
- Never claim more than the data supports. Overstatement is the fastest route to a desk reject.
- Reproducibility: a fellow graduate student should be able to reproduce every number from the information in the paper.

## Paper Structure

Standard structure for applied micro papers. Adapt when the argument requires it — some papers merge sections, add institutional context, or reorder data and strategy.

| Section | Key Requirements |
|---------|-----------------|
| 1. Title | Short, specific, informative. Pattern: "[Mechanism]: [Evidence] from [Setting]" |
| 2. Abstract | 150 words max; question, method, main result **with a number**, mechanism, implication |
| 3. Introduction | The most critical section — 60% of whether the paper gets read |
| 4. Literature review | 1-1.5 pages; organized by channel, ending with gap paragraph |
| 5. Data | One paragraph per source; summary statistics; treatment definition |
| 6. Empirical strategy | Identifying assumption in plain language; estimating equation; pre-trends |
| 7. Results | ATT + SE; economic magnitude; event-study figure |
| 8. Robustness | Alternative estimators, sample restrictions, placebo tests |
| 9. Heterogeneity | Predetermined splits, explicitly descriptive |
| 10. Mechanisms | Theoretical channels, distinguished from heterogeneity |
| 11. Conclusion | 1-1.5 pages: finding, policy, limitations, future work |
| 12. References | Alphabetical, consistent, complete |

## Title

- Short, specific, and informative. The reader should know the topic, setting, and type of evidence from the title alone.
- Avoid question marks, puns, and vague framing ("Essays on...", "Towards a...").
- Good pattern: "[Mechanism/Effect]: [Evidence Type] from [Setting]"
  - Example: "Disasters and Innovation: Firm-Level Evidence from China"

## Abstract

- 150 words maximum for most journals (some allow 200).
- Structure: (1) question, (2) setting and method in one sentence, (3) main result **with a number** (point estimate + SE), (4) mechanism or heterogeneity, (5) implication.
- No citations. No filler ("This paper contributes to the literature..."). Start with what the paper does.
- Write the abstract **last** — after the conclusion and introduction.

## Introduction

The introduction is 60% of whether the paper gets read. Structure it paragraph by paragraph:

| Paragraph | Content |
|-----------|---------|
| **1. Question + why it matters** | Open with the economic question, not background. State what the paper does in the first or second sentence. Convey why this matters for economics broadly. |
| **2. Setting and context** | Why this setting is well-suited. Describe the identifying variation informally but precisely. The reader should understand the source of exogenous variation before the data section. |
| **3. Ex ante ambiguity** | Theoretical tension — why is the sign unclear? Signals the paper isn't confirming a foregone conclusion. |
| **4. Data and identification** | One paragraph: dataset, key variables, estimation strategy. Enough for the referee to assess credibility. |
| **5. Results** | Main findings **with numbers** (point estimates + SE). Heterogeneity and mechanisms briefly. This is where the referee decides if the paper is interesting. |
| **6. Contributions** | Three maximum, numbered. Each references the specific literature it advances. Be precise: "first firm-level causal estimate of X" > "contributes to the literature on X." |
| **7. Roadmap** (optional) | If included, make it substantive. "Section 2 establishes the aggregate patenting response" > "Section 2 reviews the literature." If it adds nothing beyond section titles, delete it. |

**Pitfalls:**
- Do not open with a broad statement about the state of the world ("Climate change is one of the greatest challenges...")
- Do not announce what the paper does before explaining why it matters
- Do not duplicate the abstract
- Do not leave contributions implicit — the referee uses this paragraph to evaluate novelty

Upper limit: 5 pages. A non-specialist should understand every point.

## Literature Review

**Length and format:** Top journals either fold the lit review into the introduction (AER, QJE style) or keep a standalone section of 1-1.5 pages (JDE, JIE style). A 5-page literature survey signals a working paper, not a journal submission.

**Structure by channel/mechanism, not paper by paper:**
- Bad: "Smith (2020) finds X. Jones (2021) finds Y. Lee (2022) finds Z."
- Good: "Three mechanisms link disasters to innovation. On the disruptive side, [citations]. On the adaptive side, [citations]."

**The gap paragraph (mandatory):** The final paragraph must state: (a) what prior work has established, (b) what remains unknown, (c) precisely how this paper fills that gap. The gap must mirror the contributions in the introduction.

**What to cut:** Macro cross-country evidence that doesn't speak to your identification. Papers already cited and discussed in the introduction. Papers topically related but methodologically distant. Detailed summaries of sample sizes and coefficients for papers that aren't your closest antecedents.

**Common mistakes:**
- Using AI chat tools in chat mode to draft the lit review — they produce paper-by-paper catalogs, not integrated arguments. The lit review must be written with the full paper in mind.
- Citing papers in the intro that are never discussed in the lit review (or vice versa).
- Ending without identifying the gap.
- Never end with "this paper contributes to the growing literature on X."

## Data

- One paragraph per data source: provider, coverage (years, geography, unit of observation), key variables
- Explain merging procedures and identifiers. Reproducibility matters.
- Report sample restrictions with justification for each dropped observation
- Summary statistics table: means, SD, min, median, max — paneled by variable type (outcomes, controls, characteristics)
- Discuss summary statistics in text — flag unusual patterns (skewness, many zeros, extreme outliers)
- Define treatment precisely. If constructed (geocoding, matching, thresholds), explain step by step
- Report treated vs. control counts and how treatment varies over time
- Include map or figure showing spatial/temporal variation if relevant

**Common mistakes:** Burying restrictions in footnotes. Not explaining missing data handling. Using variables without describing them in this section.

## Empirical Strategy

- State the identifying assumption **in plain language** before writing equations
- Explain why the assumption is credible in this setting
- Present the estimating equation with every term defined
- Explain the choice of estimator. If using staggered DiD, acknowledge the TWFE bias literature
- Specify clustering level and justify it
- For DiD: show event-study plot with pre-treatment coefficients. Report the coefficients and SEs explicitly — don't just say "no evidence of pre-trends"
- Report the preferred specification without controls as benchmark. Add controls as robustness
- If controls are post-treatment ("bad controls"), acknowledge explicitly

**Common mistakes:** Reporting only the specification with controls. Not explaining what fixed effects absorb. Using TWFE in staggered settings without acknowledging the bias literature.

## Results

- Lead with the main estimate. Report ATT with standard error in parentheses
- **Never report p-values in running text.** Significance stars belong in tables only
- Interpret economic magnitude: "An 18.6 percent increase in patenting" not "significant at the 5 percent level"
- Show the event-study figure alongside the table
- Point estimates in percent when using Poisson or log specifications
- Report: "The ATT is 18.6 percent (s.e. = 0.085)" — never "statistically significant at the X percent level"

## Robustness

- Alternative estimators (stacked DiD, alternative clustering, Conley SEs)
- Sensitivity to sample restrictions (dropping outliers, varying treatment definitions)
- Placebo tests if applicable
- Do not oversell. If an alternative specification gives different results, discuss honestly

## Heterogeneity

- Shows *who* responds. It is **descriptive**, not causal, unless the dimension is itself exogenous.
- State explicitly: "These splits are descriptive and identify correlates of the response, not causal mechanisms."
- Split on **predetermined** variables (measured before treatment). Never split on post-treatment outcomes.
- Report ATTs for each subgroup with standard errors.
- Discuss the economic logic before showing results.
- Connect heterogeneity results to the mechanisms section.

**Common mistakes:** Splitting on too many dimensions without motivation. Not discussing absent effects. Treating heterogeneity as mechanisms.

## Mechanisms

- Shows **why** the effect exists — the theoretical channel.
- Distinct from heterogeneity. Heterogeneity: "large firms respond." Mechanism: "large firms respond *because they have higher internal cash flow*."
- State the hypothesis before the test.
- Report null mechanism results — they are informative.

**Common mistakes:** Conflating with heterogeneity. Testing too many mechanisms without a framework. Not reporting nulls.

## Conclusion

1-1.5 pages maximum — the shortest section of the paper.

1. Restate the main finding in one sentence
2. Summarize key heterogeneity/mechanism result
3. Policy implication (one paragraph, concrete)
4. Limitations honestly (sample, identification, external validity)
5. Future work briefly (one or two sentences, not a research agenda)

**Common mistakes:** Repeating the introduction verbatim. Overclaiming external validity. Introducing new results. Being too long.

## Style Rules for Academic Economics

- Declarative, precise, direct sentences. No hedging ("it seems," "it appears," "it could be argued")
- Active voice. "We estimate" not "It is estimated"
- No colons to introduce clauses or results in running prose. Restructure.
- No em-dashes as punctuation. Use commas or separate sentences
- No informal connectives ("Interestingly," "Importantly," "It is worth noting that")
- No vague intensifiers ("very", "extremely", "highly")
- Never start with bare "This" — follow with the noun: "This evidence indicates" not "This indicates"
- Short paragraphs. Each opens with a topic sentence stating the main claim
- Do not open sections by announcing what they do ("This section investigates..."). Open with the substantive claim
- One idea per paragraph. No paragraph longer than half a page

### Footnotes

Follow Cochrane's test:
- "Do you really want the reader to stop and read this? Then it should be in the text."
- "Do you think the average reader should not stop? Then delete the footnote."
- Acceptable: long reference lists, simple algebra, documentation details.

## Workflow

- Write the results section first, then build data and identification to support it
- Write the introduction last (or rewrite it last) — it should promise exactly what the paper delivers
- Read published papers in your target journal to calibrate length, tone, and structure
- Have someone outside your field read the introduction — if they can't state the question, finding, and contribution, rewrite it
- Always compile and proofread the PDF before circulating — broken cross-references signal carelessness
- Revise multiple times: "All drafts must be edited and polished many times" (Creedy, 2001)
- Let it rest, then return refreshed for a final polish

### Getting Inspiration

Study papers by economists known for clear writing (Daron Acemoglu, Nathan Nunn, Andrei Shleifer, and leaders in your field). "Getting inspiration" means imitating clear phrases and structures, then adapting them — this is about style, not ideas.
