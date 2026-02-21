# Agent Design Best Practices

## Core Philosophy

1. **Let the agent decide** — give tools, not pre-computed data
2. **Keep tools atomic** — one operation per tool, return structured data
3. **Instructions shape behavior** — dynamic instructions are the primary control mechanism

## Agent Design

- Agents are data definitions, not classes: name, model, instruction builder, tools, output schema
- One agent definition per file
- 3-5 tools is the sweet spot. Above 20 tools, models pick wrong tools.
- Default to a single agent. Only split when: >20 tools, conflicting instructions, or need parallelization

### Model Selection

| Use Case | Model | Why |
|----------|-------|-----|
| Extraction, simple analysis | Small/fast | Fast, cheap, structured output |
| Complex reasoning, grouping | Large | Better multi-step reasoning |
| Chat Q&A with tools | Reasoning | Best tool use + reasoning balance |

## Tool Design

Every tool MUST:

- Return **structured data** (JSON, not raw strings)
- Be **read-only** — no database writes, no side effects
- Do **one thing** (atomic)
- Have a **specific description** (the LLM reads this to decide whether to call it)

```
Bad:  "Get data"
Good: "Get all existing values for an entity type to check for duplicates before creating new ones"
```

## Instruction Design

Follow this order:

1. **Role** — who the agent is (one sentence)
2. **Context** — metadata, configuration (minimal — just IDs and names)
3. **Task** — what to extract/analyze (detailed)
4. **Tool usage** — which tools to call, in what order, efficiency guidelines
5. **Rules** — naming conventions, deduplication, edge cases
6. **Output format** — exact structure expected

### Key Rules

- NEVER pre-load content into instructions. Give a read tool + identifier instead.
- Guide tool usage explicitly — agents tend to over-use tools
- Keep instructions under 500 words
- Use dynamic instruction builders, not static strings
- Pass data as JSON, not formatted markdown

## Multi-Agent Patterns

| Pattern | When to Use | Trade-off |
|---------|------------|-----------|
| Agent-as-tool | Sub-task needs different instructions/tools | Extra API round-trip |
| Handoffs | Conversation should switch modes entirely | Original agent stops |
| Sequential | Independent pipeline steps | Each agent has own context |

## Anti-Patterns — NEVER Do

1. **Pre-load content** — Let the agent read via tools, not pre-pasted context
2. **Give agents write access** — Agent returns data; orchestration layer persists
3. **One agent per use case** — Use one generic agent configured by data
4. **Hardcode types in output models** — Use generic dicts keyed by type
5. **Split agents too early** — Default to single agent unless clear need
6. **Over-orchestrate** — A coordinator that just routes should be a function, not an agent

## Checklist

- [ ] 3-5 tools (never more than 20)
- [ ] Dynamic instruction builder (not static string)
- [ ] Clear output schema
- [ ] Model appropriate for the task
- [ ] Tools are read-only, return structured JSON
- [ ] Instructions under 500 words
- [ ] No pre-loaded content in instructions
