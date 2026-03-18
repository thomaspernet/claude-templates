---
paths:
  - "**/slides/**"
  - "**/output/**"
---

# Review and Auto-Correction Rules

## Mandatory Review Pass

After generating or modifying ANY slide content, immediately perform a full review pass. Do not wait for the user to ask — auto-correction is the default behavior.

## Review Sequence

Execute these checks in order after every slide generation:

### 1. Title Scan (Horizontal Flow)

- List all slide titles in sequence
- Read them as a standalone narrative — do they tell the full story?
- Fix any title that is a topic label instead of a conclusion
- Fix any title that breaks the narrative flow

### 2. Content Audit

- Each slide has exactly one message — split any that try to say two things
- No bullet exceeds 6 words — rewrite or split
- No slide has more than 6 bullets — move excess to a new slide or appendix
- All text is large enough to read (18pt+ body, 28pt+ titles)

### 3. Data Integrity

- Every number, percentage, or claim has a source citation
- Chart titles state the insight, not just the metric name
- Axes are labeled with units and time periods
- No 3D charts — convert to 2D

### 4. Visual Consistency

- All slides use the same font families and sizes
- Color palette is consistent — no rogue colors
- Alignment is uniform (margins, text boxes, chart positions)
- Logos and recurring elements are in the same position on every slide

### 5. Language Polish

- Fix typos and grammatical errors
- Ensure parallel structure in bullet lists
- Remove filler words ("basically", "essentially", "in order to")
- Verify acronyms are defined on first use

## Auto-Fix Protocol

When a problem is found:

1. Fix it immediately — do not just flag it
2. Briefly note what was fixed (one line per fix)
3. If a fix requires a judgment call (e.g., splitting a slide changes narrative flow), fix it and explain the choice

## When to Flag Instead of Fix

Only flag (don't auto-fix) when:

- The fix requires information you don't have (missing data source, unclear audience)
- The fix would change the core argument or recommendation
- The user explicitly asked for a specific structure you'd be overriding
