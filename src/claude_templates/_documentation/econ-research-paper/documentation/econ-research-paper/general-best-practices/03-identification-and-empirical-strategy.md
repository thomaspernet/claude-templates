# Identification and Empirical Strategy

> Distilled from Valfort (2014), Research Methodology courses, Pantheon-Sorbonne University.

## Why Identification Matters

The core challenge of empirical economics is establishing **causality**, not correlation. A naive OLS regression of Y on X almost always suffers from endogeneity — the coefficient captures more than the causal effect you want to measure.

Your empirical strategy section must:
1. **Name the endogeneity problems** explicitly (omitted variable bias, reverse causality, selection bias, measurement error)
2. **Explain your identification strategy** and why it addresses these problems
3. **Convince the reader** — this is an argument, not just a description

## Common Identification Strategies

### Instrumental Variables (IV / 2SLS)

- The instrument Z must affect Y **only through** X (exclusion restriction)
- The instrument must be correlated with the endogenous variable X (relevance)
- Present evidence for both:
  - **Relevance**: first-stage F-statistic, scatterplot of Z vs. X
  - **Exclusion**: argue why Z has no direct effect on Y; address plausible alternative channels

### Difference-in-Differences (DiD)

- Requires a treatment and control group observed before and after an intervention
- Key assumption: **parallel trends** — absent treatment, both groups would have followed the same trajectory
- Present pre-treatment trends visually
- Discuss threats: anticipation effects, composition changes, spillovers

### Regression Discontinuity (RD)

- Exploits a cutoff in a running variable that determines treatment assignment
- Present the discontinuity visually (scatter with fitted lines on both sides)
- Test for manipulation of the running variable (McCrary density test)
- Bandwidth sensitivity analysis

### Randomized Controlled Trials (RCT)

- Gold standard for internal validity, but limited external validity
- Report balance tables (treatment vs. control group characteristics)
- Discuss attrition and compliance
- Intent-to-treat (ITT) vs. local average treatment effect (LATE)

### Fixed Effects / Panel Methods

- Absorb time-invariant unobservable heterogeneity
- Discuss what remains after fixed effects are absorbed
- Consider whether the remaining variation is truly exogenous

## Presenting Your Strategy

### In the Introduction (HOW 2)

- Brief, clear explanation of the strategy
- Why it solves the key endogeneity problem
- If IV: explain in one sentence why the instrument is valid
- 1-2 paragraphs maximum

### In the Empirical Strategy Section

- Full technical detail
- Write regression equations explicitly with precise notation
- Define every variable
- Explain what each coefficient captures
- Use visual arguments (scatterplots, pre-trends, discontinuity plots)
- Discuss remaining threats to identification honestly

## Visual Arguments

Scatterplots and graphs are powerful tools to build credibility:

| Strategy | Visual Evidence |
|----------|----------------|
| IV | Scatterplot of instrument vs. endogenous variable (first stage) |
| DiD | Pre-treatment parallel trends plot |
| RD | Scatter with fitted regression lines on both sides of cutoff |
| RCT | Balance table, attrition flow chart |

## Common Pitfalls

1. **Claiming causality without identification.** Never use causal language ("A causes B", "the effect of A on B") if your strategy doesn't credibly address endogeneity.
2. **Weak instruments.** First-stage F-statistic below 10 is a red flag. Report it and discuss.
3. **Cherry-picking specifications.** Present your main specification and explain why it's preferred. Put alternatives in robustness checks.
4. **Ignoring alternative stories.** If your instrument could affect Y through a channel other than X, you must address it — either argue against it or control for it.
5. **Over-controlling.** Including "bad controls" (variables affected by the treatment) biases your estimates. Only control for pre-treatment characteristics.
