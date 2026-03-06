# Tables, Figures, and Results Presentation

> Distilled from Valfort (2014), Research Methodology courses, Pantheon-Sorbonne University.

## The Self-Explanatory Principle

> "A reader should be able to understand a table without reference to the text. The converse rule is that the text should stand by itself, even if a reader ignores the tables." — Levine

This is the single most important rule for presenting empirical results.

## Table Construction

### Required Elements

Every regression table must include:

| Element | Example |
|---------|---------|
| **Title** | "Table 4: OLS and IV estimates of the effect of teacher truancy on test scores" |
| **Column headers** | Specification labels: (1) OLS, (2) IV, (3) IV with controls |
| **Variable names** | Clear, readable names — not Stata variable codes |
| **Coefficients** | Point estimates with standard errors in parentheses |
| **Significance stars** | Define at the bottom: * p<0.10, ** p<0.05, *** p<0.01 |
| **Sample description** | N, R-squared, fixed effects included, cluster level |
| **Notes** | Data source, variable definitions, sample restrictions |

### Formatting Rules

- Standard errors in parentheses below coefficients (not t-statistics)
- Specify clustering level: "Standard errors clustered at the school level"
- Include the number of observations (N) for every column
- Report R-squared or pseudo-R-squared
- Note which fixed effects are included (country, year, school, etc.)

## Interpreting Results

### Economic Magnitude

Statistical significance alone is insufficient. Always discuss the **economic magnitude** of your results:

- **Standard deviation interpretation**: "A one standard deviation increase in X is associated with a Y% change in the outcome"
- **Policy-relevant comparison**: "The effect is equivalent to the impact of adding one additional year of schooling"
- **Percentage of the mean**: "The effect represents X% of the sample mean"

> "Especially in large panel data sets even the tiniest of effects is 'statistically significant.'" — Cochrane (2005)

### Writing About Results

- Derive main results clearly from the regression tables
- Refer to specific table numbers and columns: "Column (3) of Table 4 shows that..."
- Report exact coefficient values and significance levels
- Compare magnitudes across specifications to show robustness
- Discuss unexpected findings — don't hide them

## Descriptive Statistics

### Required Statistics

For every variable used in the analysis, present:

| Statistic | What It Shows |
|-----------|---------------|
| N | Sample size (flags missing data) |
| Mean | Central tendency |
| SD | Dispersion |
| Min | Data range and potential outliers |
| Max | Data range and potential outliers |

### Presenting Descriptive Statistics

- Group variables by type (outcome, treatment, instrument, controls)
- Comment on the statistics — don't just present the table
- Flag any unusual patterns (high missingness, extreme values, unexpected distributions)
- Compare your sample statistics to well-known benchmarks when relevant

## Figures

### Scatterplots

Use scatterplots to document key correlations:
- Instrument vs. endogenous variable (first stage visualization)
- Pre-treatment trends for DiD designs
- Regression discontinuity plots

### Best Practices

- Label axes clearly with variable names and units
- Include fitted lines where appropriate
- Add confidence intervals when possible
- Title should describe what the figure shows
- Reference each figure in the text: "As Figure 1 shows..."

## Robustness Tables

### Structure

Present robustness checks in tables that mirror your main results table:
- Same format and column structure
- Clearly label what changes in each column/panel
- Use panel labels: "Panel A: Alternative dependent variable", "Panel B: Excluding outliers"

### What to Include

Priority order:
1. **Alternative stories** — control for competing channels
2. **Alternative measures** — different definitions of key variables
3. **Alternative samples** — excluding outliers, subsample analysis
4. **Alternative specifications** — different functional forms, additional controls

## Common Mistakes

1. **Tables with Stata variable names** — Use readable labels, not `lnrgdppc_2005`
2. **Missing sample information** — Every column must report N
3. **Stars without magnitudes** — Reporting "significant at 1%" without discussing the coefficient size
4. **Inconsistent formatting** — Use the same format across all tables
5. **Figures without labels** — Every axis, every line must be labeled
6. **Results not referenced in text** — Every table and figure must be explicitly discussed
