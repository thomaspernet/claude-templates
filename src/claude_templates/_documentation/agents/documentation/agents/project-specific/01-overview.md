# Project Agent Overview

> Document your project's agent architecture here. This file should be the first place a developer or coding agent looks to understand how agents work in this project.

---

## Architecture

<!-- Describe your project's agent architecture. Example: -->

```
TODO: Replace with your project's directory structure

src/
  agents/          — Agent definitions (one per file)
  tools/           — Tool functions (grouped by domain)
  core/            — Shared models, context, configuration
  services/        — Business logic, orchestration
```

---

## Agent Inventory

<!-- List all agents in the project. Keep this table current. -->

| Agent | Model | Tools | Purpose |
|-------|-------|-------|---------|
| `example_agent` | gpt-4o-mini | search, read | Example — replace with your agents |

---

## Tool System

<!-- Describe how tools are registered and organized. -->

### Registration Pattern

```python
# TODO: Show your project's tool registration pattern
```

### Tool Categories

| Category | Tools | Purpose |
|----------|-------|---------|
| Navigation | discover, search, explore | Find and browse content |
| Content | read, get_details | Retrieve actual data |
| Context | fetch_history | Previous conversation state |

---

## Separation of Concerns

<!-- Document the boundaries between agents, tools, services, and flows. -->

- **Agents** — Pure functions: receive context, call tools, return structured output
- **Tools** — Read-only: query data, never write
- **Services** — Business logic: orchestrate agents, persist results
- **Flows** — User-facing: handle requests, build agent context, return responses

---

## Adding a New Agent

Checklist:

- [ ] Create agent definition file in `agents/`
- [ ] Define instruction builder (dynamic, not static)
- [ ] Register tools (3-5, read-only)
- [ ] Define output schema
- [ ] Add to inventory table above
- [ ] Write tests
