---
name: build-academic-deck
description: "Use this skill when creating a research or academic conference presentation. Invoke when the user says 'build a talk', 'create conference slides', 'make an academic presentation', or wants to present research findings."
---

# Build Academic Deck

## When to Use

**Perfect for:**
- Conference presentations (15-20 min talks, job market talks)
- Seminar presentations (45-60 min with discussion)
- Research group or lab meeting presentations
- Dissertation defense slides

**Not ideal for:**
- Lecture slides for a course (use a teaching template)
- Poster presentations (different format entirely)
- Non-academic audiences (use consulting or analysis modules)

---

> **Core Philosophy:** The audience remembers one thing. Design every slide to reinforce your main contribution. If a slide doesn't serve the central argument, cut it.

## CRITICAL

1. **State the research question on slide 2-3.** The audience must know what you're investigating within the first 2 minutes.
2. **Auto-review after building.** Run the academic self-review checklist and fix all issues before presenting output.

---

## Step 1: Define the Talk

- What is the **one finding** the audience should remember?
- What type of talk? (conference 15min, seminar 45min, job market 90min)
- Who is the audience? (field specialists, general economists, interdisciplinary)
- What stage is the paper? (early results, R&R, published)

## Step 2: Outline the Narrative

Follow the academic arc:

1. **Hook** (1 slide) — A fact, puzzle, or policy question that creates interest
2. **Research question** (1 slide) — Crisp, one-sentence question
3. **This paper** (1 slide) — What you do, in 3 bullets: method, data, finding
4. **Literature** (1-2 slides) — Position relative to 3-4 key papers, not a survey
5. **Empirical strategy** (2-3 slides) — Identification, data, estimation
6. **Results** (3-5 slides) — One table/figure per slide, action titles
7. **Robustness** (1-2 slides) — Key checks that address obvious concerns
8. **Conclusion** (1 slide) — Contribution + implications + limitations

**Commit outline before building slides.**

## Step 3: Build Slides

For each slide:

1. Write the action title (finding, not topic)
2. Create one visual element (table, figure, or diagram)
3. Highlight the key result with color or bold
4. Add source line (dataset, N, time period)
5. Write speaker notes with timing cues

### Table Slides

```
Title: "Trade openness increases GDP growth by 1.2pp (p<0.01)"

| | (1) OLS | (2) IV | (3) IV + Controls |
|---|---|---|---|
| Trade/GDP | 0.8** | **1.2*** | **1.1*** |
| | (0.3) | (0.4) | (0.3) |
| Controls | No | No | Yes |
| N | 1,200 | 1,200 | 1,150 |

Source: Penn World Table 10.0, 1960-2019. *** p<0.01
```

### Figure Slides

- Large figure, minimal surrounding text
- Title states the pattern: "Effect concentrates in developing economies"
- Axis labels: variable name + unit + period

## Step 4: Self-Review

Run the academic checklist:

1. Research question stated within first 3 slides
2. Identification strategy explained (mechanism, not just name)
3. Key coefficient highlighted in every results table
4. Finding-based titles on every slide
5. Slide count ≤ time slot in minutes
6. Appendix covers top 5 likely questions
7. No text-heavy slides (move prose to speaker notes)

Fix all issues. Note what was corrected.

## Step 5: Prepare for Q&A

- List the 5 most likely questions
- Map each to an appendix slide
- Write 2-sentence answers in speaker notes

## Output

A deck outline at `slides/{talk-name}/outline.md` following academic structure:

```markdown
# {Paper Title}

> {One-sentence contribution} | Venue: {conference} | Time: {minutes}min

## Slide 1 — Title
Authors, affiliations, date

## Slide 2 — Hook: {compelling fact or puzzle}
...

## Slide 3 — Research Question: {one-sentence question}
...

---
*Status: outline | draft | reviewed | final*
```
