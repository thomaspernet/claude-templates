---
name: build-analysis-deck
description: "Use this skill when creating a data analysis or insights presentation. Invoke when the user says 'present my analysis', 'create a data deck', 'build an insights presentation', or wants to turn analytical findings into slides."
---

# Build Analysis Deck

## When to Use

**Perfect for:**
- Presenting data analysis results to stakeholders
- Quarterly or monthly business reviews
- A/B test results and experiment readouts
- Market research or competitive analysis presentations

**Not ideal for:**
- Strategy recommendations without data (use consulting module)
- Academic research talks (use academic module)
- Financial modeling presentations (use finance module)

---

> **Core Philosophy:** Insight first, chart second. Every visualization must answer "so what?" If you can't state the insight in one sentence, the chart isn't ready for a slide.

## CRITICAL

1. **Lead with findings, not methodology.** The audience cares about what you found, not how you found it. Method goes in the appendix.
2. **Auto-review after building.** Run the analysis self-review checklist and fix all issues before presenting output.

---

## Step 1: Define the Analysis Story

- What business question does this analysis answer?
- Who is the audience? (data team, product managers, executives, marketing)
- What level of statistical literacy should you assume?
- What decision should this presentation enable?

## Step 2: Curate Findings

From your full analysis, select only the findings that matter:

1. List all findings from your analysis
2. Rank by relevance to the business question
3. Select the top 5-7 findings (ruthlessly cut the rest)
4. Group into 2-3 themes
5. Order themes by importance

**Rule: If it didn't change the recommendation, it doesn't need a slide.**

## Step 3: Outline

Structure the narrative:

1. **Context** (1-2 slides) — The question and why it matters
2. **Key finding** (1 slide) — The headline: one big number or statement
3. **Evidence by theme** (3-5 slides per theme) — Charts proving each theme
4. **Implications** (1 slide) — What this means for the business
5. **Recommendations** (1-2 slides) — Prioritized actions with expected impact
6. **Appendix** — Methodology, full data tables, additional cuts

**Commit outline before building slides.**

## Step 4: Build Slides

For each chart slide:

1. **Action title**: State the insight ("Churn peaks at day 7, not day 30")
2. **One chart**: Select the right type for the data relationship
3. **Callout**: Annotate the key finding directly on the chart
4. **Context**: Add benchmark, comparison, or prior period for reference
5. **Source line**: Dataset, date range, sample size
6. **Speaker notes**: The "so what" and transition to next slide

### Chart checklist per slide:
- [ ] Chart type matches data relationship
- [ ] Title states insight, not metric name
- [ ] Key data point highlighted with color
- [ ] Axes labeled with units
- [ ] Direct labels (no separate legend)
- [ ] Source line with N and date range
- [ ] Callout annotation on chart

## Step 5: Self-Review

Run the analysis checklist:

1. **Insight-first test**: Does the deck open with a finding, not a method?
2. **So-what test**: Every chart has an explicit insight callout?
3. **Chart-type test**: Each chart uses the correct type for its data relationship?
4. **Context test**: Numbers shown with benchmarks or comparisons?
5. **Declutter test**: No unnecessary gridlines, borders, legends?
6. **Recommendation test**: Actions are specific and prioritized?

Fix all issues. Note what was corrected.

## Output

A deck outline at `slides/{deck-name}/outline.md`:

```markdown
# {Analysis Title}

> {One-sentence finding} | Audience: {audience} | Question: {business question}

## Slide 1 — Context: {why this analysis matters}

## Slide 2 — Key Finding: {headline insight with number}

## Slide 3 — Theme 1: {action title with chart description}
- Chart type: {bar/line/scatter}
- Callout: {annotation text}
- Source: {dataset, N, period}

...

---
*Status: outline | draft | reviewed | final*
```
