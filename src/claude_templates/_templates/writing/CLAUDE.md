# {PROJECT_NAME}

## Project & Tech

- **Format**: Markdown
- **Conversion**: Pandoc (optional, for PDF/DOCX export)
- **Key directories**: `drafts/`, `published/`, `style/`, `assets/`

## Architecture

```
drafts/             Working documents (YYYY-MM-DD-title.md)
published/          Final versions (immutable once published)
style/              Style guide, templates, reference docs
assets/             Images, diagrams, supporting files
```

## Critical Rules

1. **One source of truth per document** — No duplicated content across files.
2. **Version drafts with dates** — Filename prefix: `YYYY-MM-DD-title.md`.
3. **Track review feedback** — Use comments or a dedicated feedback section per draft.
4. **Consistent terminology** — Define key terms once, use them identically throughout.
5. **One sentence per line** — Makes diffs meaningful and reviews easier.

## Writing Style

- Markdown: ATX headings (`#`), reference-style links, consistent list formatting
- No tabs — spaces only
- Heading hierarchy: H1 (title), H2 (sections), H3 (subsections) — no deeper
- Blank line before and after headings, lists, and code blocks
- **Prefer clarity and readability** — direct language, no unnecessary complexity
- Organize documents into **folders and subfolders** by topic — avoid many files under the same directory

## Draft Stages

1. **Outline** — Structure and key points
2. **First draft** — Get ideas down, don't self-edit
3. **Self-review** — Check structure, clarity, consistency
4. **Revision** — Incorporate feedback, refine language
5. **Final** — Proofread, format, move to `published/`

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
2. **Update `project-specific/` as part of every PR** that changes the topic area. If you add a style convention, update the style docs. Documentation updates are not optional — the work is incomplete without them.
3. **Read best practices before implementing.** Before building something new, read the relevant `general-best-practices/` doc and compare your design against it. Note intentional deviations in `project-specific/`.
4. **Keep inventories current.** If a `project-specific/` doc has an inventory table (documents, templates, style rules, etc.), it must match the codebase. Update it before starting new work if it's stale.
5. **Document decisions, not just code.** Explain *why* a style or structural choice was made. Include dates for significant decisions.

## Workflow

- Commit prefixes: `docs:`, `feat:`, `fix:`, `chore:`
- Commit at each stage transition (outline → draft → revision → final)
- When compacting context, preserve: document purpose, audience, current stage, open feedback
