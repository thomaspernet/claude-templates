---
name: synthesize-sources
description: "Use this skill after collecting notes on a topic and wanting to understand what they mean together. Invoke when the user has 3 or more source notes and wants a literature review, a synthesis, or to assess the weight of evidence — even if they don't use the word 'synthesis'."
---

# Synthesize Sources

## When to Use

**Perfect for:**
- After collecting 3+ notes on a topic in `notes/`
- Building the core argument of a literature review or research report
- Identifying gaps and contradictions across a body of sources

**Not ideal for:**
- Summarizing a single source (that belongs in `notes/`)
- Writing before enough sources are collected
- Creating a bibliography or reference list (use `references.bib`)

---

> **Core Philosophy:** A synthesis organizes by theme and argument, never by source. Summarizing each paper in turn is annotation, not synthesis. The output should read as an original analytical document that happens to cite evidence.

## ⚠️ CRITICAL

1. **Organize by theme, NEVER by source.** A synthesis that says "Author A says X, Author B says Y" is a list, not a synthesis. The document must be organized around ideas, with sources as evidence.
2. **Mark every claim with a confidence level.** `[established]` (3+ agreeing sources), `[likely]` (1-2 sources, no contradiction), `[speculative]` (single source or contested). Unmarked claims look like facts.

---

## Step 1: Inventory

- List all source notes in `notes/` relevant to the topic
- Categorize by sub-theme or perspective
- Note the source tier and reliability of each

## Step 2: Map Findings

For each key question or theme:
- What does each source say?
- Where do sources agree? (consensus)
- Where do sources disagree? (controversy)
- What is not covered? (gaps)

## Step 3: Assess Evidence

- Mark confidence levels: `[established]`, `[likely]`, `[speculative]`
- Note where triangulation is strong (3+ sources agree)
- Flag single-source claims for further investigation

## Step 4: Write Synthesis

Create a document in `synthesis/` that:
- Organizes by theme, NOT by source
- Presents the weight of evidence for each finding
- Discusses contradictions honestly
- Identifies gaps and open questions
- Cites all sources properly

## Step 5: Update

- Add new connections back to individual source notes
- Update `references.bib` if needed
- Note follow-up questions for further research

## Output

A synthesis document at `synthesis/{topic}.md`:

```markdown
# Synthesis: {Topic}

## Key Findings

### {Theme 1}
[Claim] `[established]` — (Author A, Year; Author B, Year)
[Claim] `[speculative]` — (Author C, Year) — single source, needs verification

### {Theme 2}
...

## Contradictions and Open Questions
- [Source A] and [Source B] disagree on X.
- Gap: No sources address Y.

## Confidence Summary
| Finding | Level | Sources |
|---------|-------|---------|
```
