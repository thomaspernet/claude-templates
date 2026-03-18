---
name: build-deck
description: "Use this skill when creating a presentation deck from scratch. Invoke when the user says 'build a deck', 'create a presentation', 'make slides', or wants to produce a PowerPoint deliverable."
---

# Build Deck

## When to Use

**Perfect for:**
- Creating a new presentation from scratch
- Restructuring an existing deck into proper slide format
- Converting a document, report, or analysis into a presentation

**Not ideal for:**
- Editing a single slide (edit directly)
- Reviewing an existing deck (use the review-deck command)
- Formatting-only changes with no content work

---

> **Core Philosophy:** Narrative first, slides second. A compelling story with rough slides beats polished slides with no argument. Commit the outline before designing a single slide.

## CRITICAL

1. **Commit the outline before building slides.** Never start slide content before the structure is settled. Outline = title + one-sentence key message per slide.
2. **Self-review is automatic.** After generating the deck, run the full review checklist and auto-correct all issues before presenting output to the user.

---

## Step 1: Define the Deck

- What is the purpose? (inform, persuade, decide, teach)
- Who is the audience? (executives, peers, clients, academics, investors)
- How much time? (determines slide count: ~1-2 min per slide)
- What should the audience do after? (the call to action)

## Step 2: Outline

Structure the narrative arc:

1. **Opening** — Context + the one thing the audience needs to know
2. **Body sections** — 3-5 grouped themes, each with 2-4 supporting slides
3. **Conclusion** — Key takeaways + explicit next steps or call to action
4. **Appendix** — Backup detail for Q&A

For each slide, write:
- **Title**: The action title (conclusion sentence)
- **Key message**: What this slide proves or shows
- **Evidence**: Chart / table / bullets / diagram

**Save outline as first commit before proceeding.**

## Step 3: Build Slides

For each slide in the outline:

1. Write the action title (conclusion, not label)
2. Create the body content (chart, table, or bullets — one type per slide)
3. Add source citations for every data point
4. Write speaker notes (talking points, transition to next slide)

Follow the 6×6 rule: max 6 bullets, max 6 words per bullet.

## Step 4: Self-Review (Mandatory)

Run the full review checklist from `review-autofix.md`:

1. Horizontal flow — titles tell the full story
2. Content audit — one message per slide, 6×6 respected
3. Data integrity — all numbers sourced, charts labeled
4. Visual consistency — fonts, colors, alignment uniform
5. Language polish — no typos, parallel structure, no filler

Fix all issues before presenting to the user. Note what was fixed.

## Step 5: Finalize

- Verify slide count matches time slot
- Ensure appendix has backup for likely questions
- Write a deck summary (3 sentences: context, argument, ask)

## Output

A complete deck outline at `slides/{deck-name}/outline.md`:

```markdown
# {Deck Title}

> {One-sentence purpose} | Audience: {audience} | Time: {minutes}min

## Slide 1: {Action title}
- Key message: {what this proves}
- Evidence: {chart/table/bullets}
- Source: {data attribution}

## Slide 2: {Action title}
...

---
*Status: outline | draft | reviewed | final*
```

No slide without an action title. No data without a source. No deck without a review pass.
