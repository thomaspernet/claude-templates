# {PROJECT_NAME}

## Project & Tech

- **Format**: PowerPoint (.pptx) via python-pptx, or Markdown slide decks
- **Conversion**: python-pptx (programmatic), Pandoc (Markdown → PPTX), or direct .pptx editing
- **Key directories**: `slides/`, `assets/`, `templates/`, `output/`

## Architecture

```
slides/            Source content per deck (one folder per presentation)
  {deck-name}/
    outline.md     Slide-by-slide outline (commit before building)
    notes.md       Speaker notes and talking points
    data/          Charts, tables, source data for this deck
assets/            Shared images, logos, icons, chart templates
templates/         Master slide layouts and color palettes
output/            Generated .pptx files (git-ignored)
```

## Critical Rules

1. **Outline first, slides second.** Commit a written outline (title + key message per slide) before creating any slide content. Structural rework on finished slides wastes all formatting effort.
2. **One message per slide.** Every slide communicates exactly one takeaway. If you need two points, use two slides.
3. **Action titles, not topic labels.** Slide titles are complete sentences stating the conclusion: "Revenue grew 23% YoY driven by APAC expansion" — not "Revenue Overview."
4. **Horizontal flow.** Reading only the slide titles should tell the full story. Test this by listing all titles in sequence — they must form a coherent narrative.
5. **Always self-review output.** After generating any slide or deck, re-read every slide and auto-correct: alignment, typos, title clarity, visual hierarchy, data accuracy. No slide ships without a review pass.
6. **Source every data point.** Every chart, number, or claim must have a source citation (small font, bottom of slide).

## Slide Design Principles

- **Visual hierarchy**: Size > Color > Position. The most important element is largest.
- **6×6 maximum**: No more than 6 bullet points, no more than 6 words per bullet.
- **White space is design.** Resist filling every pixel. Generous margins and spacing signal confidence.
- **Consistent palette**: 2-3 brand colors + neutrals. Never use random colors.
- **Sans-serif fonts**: Headlines 28-36pt, body 18-24pt minimum. If text is smaller than 18pt, cut content instead.
- **No 3D charts.** Flat, clean charts only. 3D distorts perception.
- **No clip art or stock clichés.** Use diagrams, icons, or real photography.
- **Animations with purpose only.** Progressive reveal to control pacing — never decorative transitions.

## Deck Structure

Every presentation follows this skeleton:

1. **Title slide** — Deck title, subtitle, date, author/team
2. **Executive summary / Agenda** — 3-5 key messages or topics
3. **Body slides** — One message per slide, grouped into logical sections
4. **Summary / Recommendations** — Restate key takeaways and next steps
5. **Appendix** — Backup slides, detailed data, methodology notes

## Self-Review Checklist — MANDATORY

Run this checklist on every deck before delivery:

- [ ] **Horizontal flow**: Titles alone tell the full story
- [ ] **One message per slide**: No slide tries to say two things
- [ ] **Action titles**: Every title is a conclusion, not a topic label
- [ ] **Font sizes**: Nothing below 18pt
- [ ] **Alignment**: All elements snap to grid, consistent margins
- [ ] **Color consistency**: Only palette colors used, no rogue colors
- [ ] **Data sourced**: Every number has a citation
- [ ] **Spelling and grammar**: Zero typos
- [ ] **Slide count**: Appropriate for time slot (~1-2 min per slide)
- [ ] **Speaker notes**: Key talking points written for every slide

## Documentation — MANDATORY

This project may contain a `documentation/` folder organized by topic (like chapters of a book). Each topic subfolder has two sections:

```text
documentation/
  {topic}/
    general-best-practices/   — Industry reference (READ-ONLY, never modify)
    project-specific/          — This project's implementation (MUST stay in sync with code)
```

### Rules

1. **Never modify `general-best-practices/`.** These are reference benchmarks shipped with the project.
2. **Update `project-specific/` as part of every PR** that changes the topic area. Documentation updates are not optional — the work is incomplete without them.
3. **Read best practices before building.** Before creating a new deck, read the relevant `general-best-practices/` docs and compare your approach against them.
4. **Keep inventories current.** If a `project-specific/` doc has an inventory table, it must match the actual decks.
5. **Document decisions, not just slides.** Explain *why* a narrative structure or visual approach was chosen.

## Workflow

- Commit prefixes: `docs:`, `feat:`, `fix:`, `chore:`
- Commit at each stage: outline → first draft → review pass → final
- When compacting context, preserve: deck purpose, audience, current stage, open review items
