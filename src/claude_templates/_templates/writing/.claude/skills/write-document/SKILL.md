---
name: write-document
description: "Guided document creation from purpose definition through outline, draft, and final."
---

# Write Document

## When to Use

**Perfect for:**
- Creating a new document from scratch
- Reformatting or restructuring existing content into a proper document
- Any document that needs to go through a review cycle before publishing

**Not ideal for:**
- Minor edits or additions to an existing document (edit directly)
- Proofreading only (that's a review task)
- Adding a single paragraph to a large document

---

> **Core Philosophy:** Structure first, words second. A well-structured rough draft is far easier to fix than polished prose with no clear argument. Commit the outline before writing a single sentence of body text.

## ⚠️ CRITICAL

1. **Commit the outline before writing the body.** Never start drafting sections before the structure is settled and committed. Structural changes to a finished draft waste all the writing effort.
2. **One source of truth.** If content needs to appear in two places, it should exist in one place and be referenced from the other. Duplicated content drifts apart and creates contradictions.

---

## Step 1: Define Purpose

- What is this document for?
- Who is the audience? (technical level, context, needs)
- What should the reader know or do after reading?
- What is the scope? (explicitly note what's NOT covered)

## Step 2: Outline

- H2 sections as main points
- 2-3 bullet points per section (key ideas)
- Logical ordering (chronological, importance, complexity)
- **Save outline as first commit before proceeding**

## Step 3: Research / Gather

- Collect supporting information, data, examples
- Note sources for citation
- Identify gaps that need more research

## Step 4: First Draft

- Write section by section following the outline
- Don't self-edit while drafting — get ideas down first
- Use placeholder markers for missing info: `[TODO: ...]`
- One sentence per line

## Step 5: Self-Review

- Fix structural issues first (wrong order, missing sections, scope creep)
- Then clarity and consistency
- Then grammar and polish
- Check against the purpose defined in Step 1

## Step 6: Revision

- Address all self-review findings
- Remove all `[TODO]` markers
- Verify all facts, figures, and citations

## Step 7: Finalize

- Final proofread
- Verify formatting (headings, lists, links)
- Move from `drafts/` to `published/`
- Commit with `docs: publish {document name}`

## Output

A complete document at `drafts/YYYY-MM-DD-{title}.md`:

```markdown
# {Title}

> {One-sentence purpose statement}

## {Section 1}
...

---
*Audience: {audience} | Scope: {scope} | Status: draft*
```

No `[TODO]` markers remaining before moving to `published/`.
