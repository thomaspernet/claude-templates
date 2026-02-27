---
name: explore-data
description: "Use this skill at first contact with any new dataset. Invoke when the user mentions a new CSV, table, or dataset they haven't analyzed yet, or reports unexpected values, missing data, or wants to understand structure before writing code — even before a specific analysis question is asked."
---

# Explore Data — Systematic EDA

## When to Use

**Perfect for:**
- First contact with a new dataset
- Diagnosing data quality issues before analysis
- Understanding structure before writing processing code

**Not ideal for:**
- Re-running known analysis on familiar data
- Building final figures or paper tables
- Profiling performance of large datasets (use specialized tools instead)

---

> **Core Philosophy:** Describe what the data *is* before deciding what to do with it. Every assumption about structure, completeness, and quality must be verified, not guessed.

## ⚠️ CRITICAL

1. **Never modify files in `data-source/`.** Raw data is immutable. If cleaning is needed, it belongs in `data-processing/` — not here.
2. **Explain patterns, not code.** The EDA output is a human-readable summary of findings, not a code walkthrough. Describe what you observe, not how you computed it.

---

## Step 1: Overview

- Shape (rows, columns)
- Column names and dtypes
- Memory usage
- First/last 5 rows

## Step 2: Missing Values

- Count and percentage of nulls per column
- Pattern analysis — are nulls random or systematic?
- Recommendation: drop, impute, or flag

## Step 3: Distributions

- `df.describe()` for numeric columns
- Value counts for categorical columns (top 10)
- Identify skewed distributions
- Check for obvious outliers (> 3 std from mean)

## Step 4: Correlations

- Correlation matrix for numeric columns
- Flag highly correlated pairs (|r| > 0.8)
- Note potential multicollinearity issues

## Step 5: Data Quality

- Duplicate rows
- Inconsistent categories (case, whitespace, encoding)
- Date parsing issues
- Suspicious values (negatives where unexpected, future dates, etc.)

## Step 6: Visualizations

- Histograms for numeric columns
- Bar charts for top categorical values
- Correlation heatmap
- Box plots for outlier detection

Save all figures to `reports/figures/eda/`.

## Output

Produce a markdown summary at `reports/eda-{dataset-name}.md`:

```markdown
# EDA: {Dataset Name}

## Summary
- Rows: X | Columns: Y | Memory: Z MB
- Key issue: [most important finding]

## Data Quality Issues
| Column | Issue | Severity | Recommendation |
|--------|-------|----------|----------------|

## Distribution Notes
[Notable skews, outliers, unexpected values]

## Correlations
[Pairs above 0.8 threshold, multicollinearity concerns]

## Recommended Next Steps
1. [Priority fix or investigation]
```
