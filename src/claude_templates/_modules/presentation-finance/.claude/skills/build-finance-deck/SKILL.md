---
name: build-finance-deck
description: "Use this skill when creating a financial presentation, investor deck, or board presentation. Invoke when the user says 'build a pitch deck', 'create an investor presentation', 'make a board deck', or wants to present financial data or projections."
---

# Build Finance Deck

## When to Use

**Perfect for:**
- Investor pitch decks and fundraising presentations
- Board meeting presentations
- Quarterly earnings or business reviews
- Investment memos and financial planning presentations

**Not ideal for:**
- Pure data analysis without financial focus (use analysis module)
- Academic research presentations (use academic module)
- Strategic recommendations without financial data (use consulting module)

---

> **Core Philosophy:** Numbers tell a story only when they have context. Every financial figure needs a comparison — to plan, to prior period, to industry, or to a competitor. A number alone is just a number; a number with context is an insight.

## CRITICAL

1. **State assumptions on every projection.** No forecast without the 2-3 key assumptions that drive it. The audience judges your thinking, not your optimism.
2. **Auto-review after building.** Run the finance self-review checklist and fix all issues before presenting output.

---

## Step 1: Define the Deck

- What type? (pitch, board, earnings, investment memo, FP&A)
- Who is the audience? (VCs, board, analysts, leadership team)
- What is the ask or decision? (funding, approval, strategic pivot)
- What is the key financial narrative? (growth, efficiency, turnaround, scale)

## Step 2: Assemble the Financial Story

Every finance presentation tells one of these stories:

- **Growth**: Revenue acceleration, market expansion, unit economics improving
- **Efficiency**: Margin expansion, cost reduction, operational leverage
- **Turnaround**: Problem acknowledged, plan in place, early proof points
- **Scale**: Proven model, path to profitability, capital-efficient growth

Pick your story and ensure every slide reinforces it.

## Step 3: Outline

### For Pitch Decks (10-12 slides):

1. **Cover** — Company, tagline, date
2. **Problem** — Pain point with customer evidence
3. **Solution** — Your product, how it works
4. **Market** — TAM/SAM/SOM with bottoms-up logic
5. **Traction** — Key metrics and milestones
6. **Business model** — Revenue model + unit economics
7. **Financials** — 3-year projection + assumptions
8. **Team** — Founders + key hires
9. **Ask** — Amount, use of funds, milestones unlocked
10. **Appendix** — Detailed financials, competitive landscape

### For Board Presentations (15-20 slides):

1. **Executive summary** — Performance vs. plan, 3 key items for discussion
2. **Financial performance** — Revenue, margins, cash flow vs. budget
3. **Segment deep dives** — Per business unit or product line
4. **Strategic initiatives** — Progress on key projects
5. **Risks and mitigations** — What could go wrong and what you're doing about it
6. **Outlook and decisions** — Next quarter guidance, items needing board input

**Commit outline before building slides.**

## Step 4: Build Slides

For each financial slide:

1. **Action title**: State the financial insight ("Revenue grew 35% YoY, ahead of 25% plan")
2. **One exhibit**: Chart or table with proper financial formatting
3. **Benchmark**: Show comparison (vs. plan, prior period, industry)
4. **Assumptions**: List 2-3 key drivers if it's a projection
5. **Source line**: Data source and date
6. **Speaker notes**: Key talking points and backup for questions

### Financial table template:

```
Title: "Revenue on track to exceed plan by 12% for FY26"

|              | FY24 (A) | FY25 (A) | FY26 (F) | YoY Growth |
|--------------|----------|----------|----------|------------|
| Revenue      | $4.2M    | $5.8M    | $8.1M    | 40%        |
| Gross Margin | 62%      | 65%      | 68%      | +3pp       |
| EBITDA       | ($0.5M)  | $0.1M    | $0.8M    | —          |

Assumptions: 15% price increase, 20% volume growth, 2 new enterprise deals
Source: Internal financials, Feb 2026. (A) = Actuals, (F) = Forecast
```

## Step 5: Self-Review

Run the finance checklist:

1. **Assumptions stated**: Every projection has explicit drivers
2. **Benchmarked**: Numbers compared to plan, prior period, or industry
3. **Consistent units**: Same $K/$M/$B and decimal places throughout
4. **Actuals vs. forecast**: Clearly distinguished (labeling or formatting)
5. **Growth rates shown**: YoY or QoQ alongside absolutes
6. **Risks acknowledged**: At least one slide on risks/mitigations
7. **Ask is clear**: Specific amount, use of funds, milestones (for pitch decks)

Fix all issues. Note what was corrected.

## Output

A deck outline at `slides/{deck-name}/outline.md`:

```markdown
# {Deck Title}

> {One-sentence financial narrative} | Type: {pitch/board/earnings} | Date: {date}

## Slide 1 — Cover
{Company}, {Tagline}, {Date}

## Slide 2 — {Action title with key financial headline}
- Key metric: {number with comparison}
- Assumptions: {if projection}
- Source: {data source}

...

---
*Status: outline | draft | reviewed | final*
```
