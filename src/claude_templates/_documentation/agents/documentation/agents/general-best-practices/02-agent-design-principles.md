# Agent Design Principles

> General best practices for designing LLM-based agents, tools, and instructions. Not specific to any application or SDK.

---

## 1. Core Philosophy

Agents work best when they have **clear goals**, **focused tools**, and **minimal pre-loaded context**. The orchestration layer should set up the agent with the right configuration, then let the agent decide how to accomplish its goal through tools.

Three principles:

1. **Let the agent decide** -- give tools, not pre-computed data
2. **Keep tools atomic** -- one operation per tool, return structured data
3. **Instructions shape behavior** -- dynamic instructions are the primary control mechanism

---

## 2. Agent Design

### Agents are Declarative

An agent is a data definition, not a class. Define the agent with a name, model, instruction builder, tool list, and output schema. Register it at module level so it's available by name.

### Naming

- Agent names: `snake_case`, descriptive -- `extraction_agent`, `chunking_strategy_agent`
- One agent definition per file
- File structure: `agents/{domain}/{agent_name}.py`

### Model Selection

| Use Case | Model Class | Why |
| --- | --- | --- |
| Extraction, simple analysis | Small/fast model | Fast, cheap, structured output |
| Complex reasoning, grouping | Large model | Better reasoning for multi-step |
| Chat Q&A with tools | Reasoning model | Best tool use + reasoning balance |

### Tool Count

Give agents **only the tools they need**. 3-5 tools is the sweet spot. More tools = more confusion, slower execution, higher cost.

Above 20 tools, models lose track of available options and pick wrong tools.

---

## 3. Tool Design

### The Tool Contract

Every tool should:
- Be **async** (if the platform supports it)
- Return **structured data** (JSON, not raw strings)
- Be **read-only** -- no database writes, no side effects
- Do **one thing**

### Tool Description Quality

The description is what the LLM reads to decide whether to call the tool. Make it specific:

```
Bad:  "Get data"
Good: "Get all existing values for an entity type to check for duplicates before creating new ones"
```

### Parameter Documentation

Even if the SDK infers the schema from function signatures, explicit parameter descriptions help with documentation and debugging:

```
"query (str): Search terms. target (str): 'notes', 'entities', or 'insights'. limit (int, optional): Max results"
```

### Return Format

Always return structured data. Include enough context for the agent to reason:

```json
{
  "entity_type": "topic",
  "count": 42,
  "values": [{"name": "Machine Learning", "uuid": "..."}]
}
```

Avoid returning raw data dumps or unstructured strings.

### Tool Categories

Organize tools by domain (e.g., `navigation`, `extraction`, `knowledge`, `context`). This helps documentation and makes it clear which tools serve which purpose.

---

## 4. Instruction Design

### Always Use Dynamic Instructions

Static strings cannot adapt to runtime context. Use callable instruction builders that receive context and produce the instruction string at runtime.

### Instruction Structure

Follow this order:

1. **Role** -- who the agent is (one sentence)
2. **Context** -- metadata, configuration (minimal -- just IDs and names)
3. **Task** -- what to extract/analyze (detailed, with types and descriptions)
4. **Tool usage** -- which tools to call, in what order, with efficiency guidelines
5. **Rules** -- naming conventions, deduplication rules, edge cases
6. **Output format** -- exact structure expected

### Let the Agent Discover Content

Do NOT pre-load content into instructions. Give the agent a read tool and an identifier:

```
Bad:  Load content in code, paste into instructions
Good: Pass a UUID, tell the agent to call read(uuid) to get content
```

Why:
- The agent can decide how much to read
- If content is too long, the agent can search within it
- Instructions stay small (not bloated with content)
- The pattern works for any content size

### Guide Tool Usage Explicitly

Agents tend to over-use tools. Be explicit about efficiency:

```
"You have a limited number of turns. Be efficient.
1. Call read(uuid) ONCE to get the content.
2. Call get_existing_values() only for types relevant to this content.
3. Produce your output as soon as possible."
```

### Pass Data as JSON, Not Formatted Markdown

The agent understands structured JSON. Don't over-format instructions with markdown sections -- pass data directly as JSON. This makes configurations transparent and editable without modifying instruction builders.

---

## 5. Output Models

### Generic Over Hardcoded

Design output models that work across multiple configurations:

```
Bad:  Hardcoded fields per type (topics: List[str], technologies: List[str])
Good: Generic dict keyed by type (entities: Dict[str, List[str]])
```

Adding a new type should mean adding data to a config, not modifying the output model.

### Strict Mode

If your SDK supports strict JSON schema mode, be aware it may reject optional fields and defaults. Use non-strict mode for practical schemas with optional fields.

---

## 6. Anti-Patterns

### Do NOT pre-load content into context

Let the agent decide what to read via tools. Code that pre-loads content removes the agent's ability to reason about what it needs.

### Do NOT give agents write access

Agent tools should be read-only. The agent returns structured data; the orchestration layer persists it. This keeps the agent pure and testable.

### Do NOT create one agent per use case

Instead of proliferating agents (one per entity type, one per document type), use one generic agent configured by data. New use cases should mean new configuration, not new agents.

### Do NOT hardcode types in output models

Use generic structures (dictionaries keyed by type) so adding new types requires only config changes.

### Do NOT over-use tools in instructions

Guide agents to the minimum necessary tool calls. "Call everything" instructions waste tokens and time.

---

## 7. Multi-Agent Patterns

### When to Use Multiple Agents

**Default to a single agent.** Only split into multiple agents when:

1. **Context pollution** (>20 tools or conflicting instructions) -- Agent picks wrong tools because descriptions overlap, or instructions for one task confuse another.

2. **Parallelization** (independent sub-tasks) -- Multiple agents can run concurrently on independent work (e.g., analyze 5 documents in parallel).

3. **Specialization** (fundamentally different capabilities) -- Tasks require different models, context windows, or tool sets.

If none of these apply, keep it as one agent. Adding agents adds latency (each call is an API round-trip) and loses shared context.

### Composition Patterns

| Pattern | When to Use | Trade-off |
| --- | --- | --- |
| **Agent-as-tool** | Sub-task needs different instructions/tools but should return results to parent | Extra API round-trip per call |
| **Handoffs** | Conversation should switch modes entirely | Original agent stops, new one takes over |
| **Sequential (flow-level)** | Independent steps in a pipeline | Each agent has its own context |

### Multi-Agent Anti-Patterns

- **Splitting too early**: Adding agents "just in case" adds latency and complexity without benefit.
- **Over-orchestration**: A coordinator that just routes to sub-agents without doing work should be a routing function, not an agent.
- **Agents that should be tools**: If a "sub-agent" always does the same thing with the same inputs, it should be a tool function.
- **Shared state assumptions**: Agents don't share memory. Pass data explicitly via context fields or tool return values.

---

## 8. Data-Driven Configuration

### Configs Over Hardcoded Agents

Instead of one agent per use case, use one generic agent with runtime configs. Configs define what to extract, how to present results, and which types are enabled.

Key principles:
- Configs are stored in the database and editable from a UI
- Code constants serve as seed data only
- Adding a new use case = adding a new config, not writing new agent code
- The instruction builder reads configs from context to build dynamic sections

### Entity/Type Registries

Map type keys to operations (repository methods, save methods, etc.) so adding a new type means adding a registry entry, not modifying agent logic.

---

## Quick Reference Checklist

### Agent Checklist
- [ ] 3-5 tools (never more than 20)
- [ ] Dynamic instruction builder (not static string)
- [ ] Clear output schema
- [ ] Model appropriate for the task
- [ ] One agent definition per file

### Tool Checklist
- [ ] Read-only (no writes, no side effects)
- [ ] Returns structured data (JSON)
- [ ] Does one thing
- [ ] Specific, descriptive name and description
- [ ] Parameters documented

### Instruction Checklist
- [ ] Role + Context + Task + Tool usage + Rules + Output format
- [ ] No pre-loaded content (agent reads via tools)
- [ ] Explicit efficiency guidance for tool usage
- [ ] Dynamic (built from runtime context)
- [ ] Under 500 words
