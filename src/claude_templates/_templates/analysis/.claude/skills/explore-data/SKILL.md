---
name: explore-data
description: "Systematic exploratory data analysis. Use when starting work with a new dataset."
---

# Explore Data — Systematic EDA

Perform a thorough exploration of the dataset. Follow each step.

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

Produce a summary markdown document with findings, issues, and recommendations for next steps.
