# Evaluating Specific Econometric Designs

> Checklist-style guidance for assessing the identification strategy in applied micro papers.

## Difference-in-Differences (DiD)

### Key Questions

- Is treatment timing truly exogenous, or could anticipation effects bias estimates?
- In staggered settings, is the paper using modern estimators (Sun-Abraham, Callaway-Sant'Anna, stacked DiD) or naive TWFE?
- Are pre-trends flat? If not, how does the paper address this?
- Is treatment absorbing? If firms/units can be treated multiple times, is this handled?
- Is SUTVA plausible? Could treated units affect control units (spatial spillovers, general equilibrium effects)?

### What to Check

- Bacon decomposition to assess the share of problematic comparisons
- Event-study coefficients with confidence intervals
- Robustness to alternative control groups (never-treated vs. not-yet-treated)
- Sensitivity to dropping specific cohorts or time periods
- Whether pre-trend coefficients and SEs are reported explicitly (not just "no evidence of pre-trends")

## Instrumental Variables (IV)

### Key Questions

- Is the exclusion restriction plausible? Can you think of a channel through which the instrument affects the outcome other than through the endogenous variable?
- Is the instrument strong? (F-statistic > 10 for single instrument; effective F for multiple instruments)
- Does the LATE interpretation make sense? Who are the compliers?

### What to Check

- First-stage regression with coefficient and F-statistic
- Reduced-form estimate (instrument directly on outcome)
- Overidentification tests if multiple instruments
- Sensitivity to instrument definition
- Whether the paper discusses who the compliers are

## Regression Discontinuity (RDD)

### Key Questions

- Is the running variable truly continuous? Are there mass points?
- Is there evidence of manipulation around the cutoff?
- Is the bandwidth choice justified and are results robust to alternative bandwidths?

### What to Check

- McCrary density test for manipulation
- Balance of covariates at the cutoff
- Sensitivity to polynomial order and bandwidth
- Donut RDD if manipulation is a concern
- Whether the local treatment effect generalizes beyond the cutoff neighborhood

## Count Data / Poisson Models

### Key Questions

- Is the conditional mean correctly specified?
- Are there many zeros? How are they handled?
- Is overdispersion a concern? (Poisson is consistent under overdispersion but SEs may need adjustment)
- Are results compared to linear alternatives (OLS on levels, log(1+Y))?

### What to Check

- Whether the paper avoids log(1+Y) transformation (introduces bias)
- Whether fixed-effects Poisson is used instead of FE negative binomial (which is inconsistent with true FE)
- Interpretation of coefficients as semi-elasticities
- Whether zeros are structural or sampling zeros

## Panel Methods / Fixed Effects

### Key Questions

- What does the within-variation look like after absorbing fixed effects?
- Is the remaining variation truly exogenous?
- Are fixed effects at the right level (firm, firm-year, industry-year)?
- Is there enough within-unit variation to identify the effect?

### What to Check

- Whether the paper reports the R-squared from the within transformation
- Whether adding more granular fixed effects changes the estimate substantially
- Whether clustered standard errors are at the right level

## Common Red Flags Across All Designs

1. **No reduced form.** If the paper uses IV, the reduced form (instrument → outcome) should be reported
2. **Pre-trends reported only visually.** Coefficients and SEs must be in a table, not just a figure
3. **Only one specification.** A single regression without alternatives is a red flag
4. **Post-treatment controls.** Variables affected by treatment bias the estimate
5. **Selective robustness.** If robustness checks only test things unlikely to change the result, they are cosmetic
6. **Missing heterogeneity.** "The effect is X on average" leaves open who gains and who loses
7. **Mechanisms without evidence.** "We argue the channel is Y" without a test is assertion, not analysis
