---
name: build-consulting-deck
description: "Use this skill when creating a consulting-style presentation or strategy deck. Invoke when the user says 'build a consulting deck', 'create a strategy presentation', 'make a client deck', or wants to produce a McKinsey/BCG/Bain-style deliverable."
---

# Build Consulting Deck

## When to Use

**Perfect for:**
- Client deliverables and strategy recommendations
- Board presentations and executive briefings
- Business case or investment proposals
- Internal strategy documents that need to stand alone

**Not ideal for:**
- Academic talks (use presentation-academic module)
- Quick team updates or stand-ups (too heavyweight)
- Data exploration presentations (use presentation-analysis module)

---

> **Core Philosophy:** Lead with the answer. The executive summary must contain your full recommendation — everything after it is evidence. If the CEO reads only slide 2, they should know what to do.

## CRITICAL

1. **Pyramid Principle: answer first, evidence second.** Never build up to a conclusion. State the recommendation, then prove it.
2. **Auto-review is mandatory.** After generating the deck, run the consulting self-review checklist and fix all issues before presenting output.

---

## Step 1: Define the Engagement

- What decision does this deck drive? (invest, cut, hire, reorganize, launch)
- Who is the primary audience? (C-suite, board, middle management, client team)
- What is the read-out format? (live presentation, leave-behind, email attachment)
- What is the one recommendation?

## Step 2: Write the Executive Summary First

Use the SCR framework:

```
SITUATION: [What everyone agrees on — market context, current state]
COMPLICATION: [What changed — threat, opportunity, gap, risk]
RESOLUTION: [Your recommendation — specific, actionable, with expected impact]
```

The Resolution should be 60-70% of the exec summary. Include:
- The recommendation (1 sentence)
- 3 supporting reasons (1 sentence each, MECE)
- Expected impact (quantified if possible)
- Immediate next step

**Commit the executive summary before building the body.**

## Step 3: Outline the Argument

Structure as a pyramid:

```
Recommendation (Slide 2: Executive Summary)
├── Reason 1 (Slides 3-5)
│   ├── Evidence A
│   └── Evidence B
├── Reason 2 (Slides 6-8)
│   ├── Evidence C
│   └── Evidence D
└── Reason 3 (Slides 9-11)
    ├── Evidence E
    └── Evidence F
```

Each "Reason" = a section header slide. Each "Evidence" = a content slide with one exhibit.

Check: Are the reasons MECE? (no overlaps, no gaps)

## Step 4: Build Slides

For each content slide:

1. **Action title**: One sentence stating the conclusion this slide proves
2. **Exhibit**: One chart, table, or framework that provides the evidence
3. **Callout**: Annotate the exhibit — circle, arrow, or text box highlighting the key insight
4. **Source line**: Data attribution at bottom
5. **Speaker notes**: Talking points for live presentation

### Exhibit Guidelines

- Charts: Annotate the insight ("Revenue peaked in Q3 before declining 15%")
- Tables: Bold or color the key row/column
- Frameworks: Use standard 2×2 matrices, waterfall charts, Harvey balls
- Process flows: Left-to-right or top-to-bottom, max 5-7 steps

## Step 5: Self-Review

Run the consulting checklist:

1. **Standalone test**: Does the deck make sense without a presenter?
2. **Titles-only test**: Read just the titles — full argument?
3. **MECE test**: No overlapping arguments, no logical gaps?
4. **Exec summary test**: Slide 2 alone = 80% of the value?
5. **Action test**: Recommendations specify who does what by when?
6. **Annotation test**: Every chart has a callout highlighting the insight?
7. **Pixel test**: Alignment, spacing, fonts perfectly consistent?

Fix all issues. Note what was corrected.

## Output

A deck outline at `slides/{deck-name}/outline.md`:

```markdown
# {Deck Title}

> {One-sentence recommendation} | Client: {name} | Date: {date}

## Slide 1 — Cover
{Client}, {Project Title}, {Date}, Confidential

## Slide 2 — Executive Summary
Situation: {context}
Complication: {what changed}
Resolution: {recommendation + 3 reasons + impact}

## Slide 3 — Section: {Reason 1}
...

---
*Status: outline | draft | reviewed | final*
```
