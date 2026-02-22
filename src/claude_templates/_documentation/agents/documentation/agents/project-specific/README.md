# Project-Specific Agent Documentation

This folder tracks how **this project** implements agents, tools, and instructions. It serves as both a human-readable reference and a benchmark the coding agent uses when implementing or improving features.

## How to Use This Folder

1. **Create files that document your project's current state** — architecture, agent inventory, tool catalog, instruction patterns, etc.
2. **Reference the general best practices** in `../general-best-practices/` as the benchmark.
3. **Keep docs in sync with code** — update this folder whenever you add, change, or remove agents, tools, or instructions.

## Suggested Structure

Start with the files that match your project's scope. Not all are needed.

| File | Purpose | When to Create |
|------|---------|----------------|
| `01-overview.md` | Architecture, directory structure, agent inventory | Always — start here |
| `02-best-practices.md` | Project-specific implementation patterns and checklists | When you have established patterns |
| `03-tool-reference.md` | Complete tool catalog with parameters and return types | When you have 5+ tools |
| `04-instruction-patterns.md` | How instructions are built, what context they receive | When using dynamic instruction builders |
| `05-memory-and-context.md` | How the project manages memory, conversation history, context | When implementing memory systems |

## Writing Guidelines

- **Be specific.** Reference actual file paths, class names, and function signatures.
- **Show the pattern, not just the rule.** Include code examples of correct implementations.
- **Add checklists.** End each doc with a checklist for adding new agents/tools/routes.
- **Date your decisions.** Note when architectural choices were made and why.

## Keeping This Folder Updated

The coding agent should update this folder as part of feature work:

- **Adding a new agent?** Update `01-overview.md` inventory table and add implementation details to `02-best-practices.md`.
- **Adding a new tool?** Update `03-tool-reference.md` with parameters, return types, and usage notes.
- **Changing architecture?** Update `01-overview.md` and note the change with a date.
- **Found a pattern that works?** Add it to `02-best-practices.md` with a code example.
- **Found an anti-pattern?** Add it with an explanation of why it fails.
