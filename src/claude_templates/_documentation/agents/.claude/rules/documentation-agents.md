# Agent Documentation — Mandatory Maintenance

This project maintains structured documentation in `documentation/agents/`. Keeping it current is **not optional** — it is part of every feature, refactor, and bugfix that touches agents, tools, or instructions.

## Folder Structure

```
documentation/agents/
  general-best-practices/   — Industry best practices (READ-ONLY reference)
  project-specific/          — This project's implementation (MUST be kept in sync with code)
```

## Rules

### 1. Never modify `general-best-practices/`

These are reference documents shipped with the project template. Treat them as read-only benchmarks. If you disagree with a practice, document the deviation in `project-specific/`, do not edit the original.

### 2. Documentation updates are mandatory, not optional

Every PR or commit that changes agent behavior MUST include corresponding documentation updates. This applies to:

- Adding, removing, or renaming an agent
- Adding, removing, or changing a tool (parameters, return types, description)
- Changing instruction builders or prompt structure
- Modifying memory, context management, or conversation handling
- Changing model selection or tool routing logic
- Fixing a bug that reveals a pattern worth documenting

If the code change touches agents/tools/instructions and the PR does not update `documentation/agents/project-specific/`, the work is incomplete.

### 3. Read best practices before implementing

Before implementing a new agent, tool, or instruction pattern, read the relevant doc in `general-best-practices/`:

| Task | Read first |
|------|-----------|
| New agent | `02-agent-design-principles.md` — agent design, tool count, output models |
| New tool | `02-agent-design-principles.md` — tool contract, descriptions, return format |
| New instructions | `01-writing-ai-instructions.md` — layers, structure, common mistakes |
| Chatbot/interactive agent | `03-chatbot-and-tool-patterns.md` — routing, think tool, streaming |
| Memory/context changes | `04-memory-in-agentic-ai.md` — patterns, context management, compaction |

Note intentional deviations from best practices in the project-specific docs with a brief rationale.

### 4. Keep the inventory current

The agent inventory table in `project-specific/01-overview.md` is the source of truth for what agents exist, what tools they use, and what model they run on. Before starting new agent work:

1. Check if the inventory matches the codebase
2. If it doesn't, update it first
3. Then proceed with the new work

### 5. What to document

For each change, update the appropriate project-specific file:

| Change | Update |
|--------|--------|
| New agent | `01-overview.md` inventory table, add to `02-best-practices.md` if new patterns |
| New tool | `03-tool-reference.md` (create if doesn't exist) |
| Architecture change | `01-overview.md` architecture section, date the decision |
| New pattern discovered | `02-best-practices.md` with code example |
| Anti-pattern discovered | `02-best-practices.md` with explanation of why it fails |
| Memory/context change | `05-memory-and-context.md` (create if doesn't exist) |

### 6. Documentation quality standards

- **Be specific.** Reference actual file paths, class names, function signatures — not abstract descriptions.
- **Show code.** Include code examples of correct implementations, not just prose rules.
- **Add checklists.** End each doc with a checklist for the relevant workflow (adding agents, adding tools, etc.).
- **Date decisions.** When documenting an architectural choice, include the date and rationale.
- **Keep it concise.** Documentation should be a quick reference, not a novel. If a section exceeds 200 lines, split it.
