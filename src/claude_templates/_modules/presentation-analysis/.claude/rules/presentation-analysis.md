# Analysis Presentation — Best Practices

## General Principles

Analysis presentations translate data into decisions. The audience is not interested in your methodology — they want insights and implications. Lead with findings, support with evidence, and end with recommendations. Every chart must answer "so what?"

## Narrative Structure

Follow the insight-driven narrative arc:

1. **Context** — What question are we answering and why now?
2. **Key finding** — The headline insight, stated upfront
3. **Evidence** — Charts and tables that prove the finding
4. **Implications** — What this means for the business or decision
5. **Recommendations** — What to do next, prioritized

Never structure as "here's what I did" (methodology-first). Structure as "here's what I found" (insight-first).

## Data Visualization Rules

### Chart Selection

| Data Relationship | Chart Type | When to Use |
|-------------------|-----------|-------------|
| Comparison | Bar chart (horizontal for many categories) | Comparing discrete items |
| Trend over time | Line chart | Showing change across periods |
| Distribution | Histogram or box plot | Understanding data spread |
| Composition | Stacked bar or 100% stacked bar | Part-to-whole relationships |
| Correlation | Scatter plot | Relationship between two variables |
| Geospatial | Choropleth map | Geographic patterns |
| Ranking | Sorted horizontal bar | Ordering items by value |
| Never | Pie chart, 3D chart, dual-axis | Distort perception, hard to read |

### Chart Design

- **Title = the insight.** "Churn concentrates in first 30 days" not "Churn by Day"
- **Label directly.** Put labels on data points, not in a separate legend
- **Highlight the story.** Color the key series/bar; grey out the rest
- **Declutter.** Remove gridlines, borders, and backgrounds unless they add meaning
- **Include units.** Every axis must have a label with units (%, $M, users)
- **Show your N.** Sample size on every chart, either in subtitle or source line

### Table Design

- Max 5 columns, 7 rows on a slide. Larger tables go to appendix.
- Bold or color the row/column being discussed
- Align numbers right, text left
- Include totals or averages where useful
- Round consistently (no "1,234,567.89" — use "1.2M")

## Insight Callouts

Every chart or table needs an explicit callout — a text annotation that tells the audience what to see:

- Use an arrow, circle, or highlighted box on the chart
- State the insight next to it: "↑ 3× increase after campaign launch"
- Never show a chart and expect the audience to find the insight themselves

## Slide Types for Analysis Decks

| Slide Type | Content |
|------------|---------|
| Context setter | The business question + why it matters now |
| Key metric | One big number + trend direction + comparison |
| Deep dive chart | One chart + insight callout + implication |
| Comparison | Side-by-side or small multiples showing contrast |
| Summary | 3-5 bullet findings with impact quantified |
| Recommendation | What to do + expected impact + owner + timeline |

## Common Mistakes to Avoid

- Leading with methodology instead of findings
- Showing every analysis you ran instead of curating the 5-6 most important
- Charts with no "so what?" annotation
- Using dual-axis charts (they confuse more than they clarify)
- Showing raw data instead of summarized insights
- Pie charts for comparing values (bar charts are always clearer)
- Missing units on axes
- No context for numbers (is 12% good or bad? Compare to benchmark)

## Self-Review — Analysis Specific

After building the deck, verify:

- [ ] Opens with the finding, not the methodology
- [ ] Every chart has an insight-based title and a callout annotation
- [ ] Chart type matches the data relationship (see selection table)
- [ ] Numbers have context: benchmarks, comparisons, or trends
- [ ] No dual-axis charts, no pie charts, no 3D charts
- [ ] Axes labeled with units, sample size noted
- [ ] Recommendations are specific and prioritized
- [ ] Appendix has methodology details for those who want them
- [ ] Color palette is consistent across all charts
- [ ] Direct labels used instead of legends where possible
