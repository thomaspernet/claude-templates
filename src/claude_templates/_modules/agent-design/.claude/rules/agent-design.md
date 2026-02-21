# Agent Design Best Practices

## Core Philosophy

1. **Let the agent decide** — give tools, not pre-computed data
2. **Keep tools atomic** — one operation per tool, return structured data
3. **Instructions shape identity; tool descriptions shape routing** — separate what the agent is from how it acts

## The Claude Code Architecture (Reference Model for Chatbots)

Claude Code is one of the most capable coding agents available. Its architecture is a proven reference model for building any interactive chatbot agent. The key insight: Claude Code succeeds not because of complex orchestration, but because of a simple, principled architecture.

### How Claude Code Works

1. **Minimal base instructions (~200 words)**: Identity, principles, behavioral guidelines. No scripts, no "when user asks X do Y." The agent reasons from principles.
2. **Tool descriptions carry routing logic**: Each tool has a rich description explaining when and why to use it. The agent reads all descriptions and picks the right tool. Adding a new tool = automatic new capability, zero instruction changes.
3. **User-configurable project settings**: `CLAUDE.md` (instructions), `.claude/rules/` (rules), skills (reference material). Users shape agent behavior through configuration, not code changes.
4. **Progressive disclosure**: Not everything loaded upfront. Base instructions always present. Project-specific knowledge loaded on demand when the agent decides it needs it.
5. **Think tool**: A no-op scratchpad the agent uses to reason before acting. Makes planning visible in logs.

### The Three Configuration Layers (Mirroring Claude Code)

| Your Chatbot | Claude Code Equivalent | When Loaded |
|---|---|---|
| **Instruction** (identity, role) | `CLAUDE.md` | Always in system prompt |
| **Rule** (constraints, formatting) | `.claude/rules/` | Always in system prompt |
| **Knowledge** (reference docs, skills) | Skills / reference docs | On demand via tool |

This separation matters because:
- Instructions define **who** the agent is (persona anchor)
- Rules define **how** it must behave (testable constraints)
- Knowledge provides **what** it can reference (loaded only when needed, so the system prompt stays lean)

### Why This Architecture Works

1. **Adaptable**: The agent handles novel question types because it reasons from principles and tool descriptions, not hardcoded scripts.
2. **Customizable**: Users shape agent behavior without code changes — just like editing CLAUDE.md.
3. **Maintainable**: Adding a new tool automatically makes it available. No instruction updates needed.
4. **Lean**: System prompt stays small. Knowledge loads on demand.
5. **Transparent**: Every instruction the chatbot receives is visible and editable by the user. No hidden prompts, no mystery behavior.

---

## Two Agent Archetypes

Most agents fall into one of two categories. The design patterns differ significantly.

| | Processing Agent | Interactive Chatbot |
|---|---|---|
| **Purpose** | Extract, classify, transform | Converse, research, advise |
| **Output** | Structured JSON (schema) | Streamed free text |
| **Tools** | 3-5 focused tools | 5-10 complementary tools |
| **Instructions** | Task-specific, developer-written | Identity-focused, user-configurable |
| **Think tool** | Usually not needed | Recommended |
| **Session** | Stateless (one run) | Stateful (conversation history) |

Design decisions below are annotated with [Processing], [Chatbot], or [Both] where the guidance differs.

## Agent Design

- Agents are data definitions, not classes: name, model, instruction builder, tools, output schema
- One agent definition per file
- [Both] 3-5 tools for processing agents. 5-10 for chatbots. Above 20 tools, models pick wrong tools.
- Default to a single agent. Only split when: >20 tools, conflicting instructions, or need parallelization

### Model Selection

| Use Case | Model Class | Why |
|----------|-------------|-----|
| Extraction, simple analysis | Small/fast | Fast, cheap, structured output |
| Complex reasoning, grouping | Large | Better multi-step reasoning |
| Chat Q&A with tools | Reasoning | Best tool use + reasoning balance |

## Tool Design

Every tool MUST:

- Return **structured data** (JSON, not raw strings)
- Be **read-only** — no database writes, no side effects
- Do **one thing** (atomic)
- Have a **rich description** that explains **when** and **why** to use the tool

### Tool Descriptions as Routing Logic [Chatbot]

The most common mistake in chatbot design is putting tool routing logic into instructions ("when the user asks X, call tool Y"). Instead, put routing intelligence in tool descriptions. The agent reads all descriptions and picks the right tool based on the question.

```
Bad:    "Search the database"
OK:     "Search notes by keyword or semantic similarity"
Good:   "Find notes, entities, or insights by keyword or semantic search.
         Use target='notes' for documents, target='entities' for concepts
         like topics or methodologies, target='insights' for extracted
         findings like summaries or key points."
```

Why this works:
- New tools automatically become available without instruction changes
- The agent adapts to novel question types
- Tool descriptions are maintained alongside tool code

### Complementary Tool Sets [Chatbot]

Design tools that cover different access patterns:

| Pattern | Tool | Purpose |
|---------|------|---------|
| **Overview** | discover | What exists? (counts, categories, types) |
| **Search** | search | Find by content (keyword or semantic) |
| **Navigate** | explore | See connections from a node |
| **Read** | read | Get actual content |
| **Detail** | get_details | Specific metadata about a node |
| **Context** | fetch_history | Previous conversation actions |

These compose naturally: discover -> search -> explore -> read -> get_details.

## The Think Tool [Chatbot]

A no-op scratchpad: the agent calls `think(thought="...")` to reason before acting. The thought is stored in tool call history and visible to the agent's context, but produces no output for the user.

- Forces the agent to plan before calling tools (reduces wasted calls)
- Makes reasoning visible in logs for debugging
- Research shows think tools improve complex task performance by ~54%

Include it for any agent with >5 tools or multi-step reasoning. Skip it for simple agents with 1-2 tools.

## Instruction Design

### Processing Agents [Processing]

Follow this order:

1. **Role** — who the agent is (one sentence)
2. **Context** — metadata, configuration (minimal — just IDs and names)
3. **Task** — what to extract/analyze (detailed)
4. **Tool usage** — which tools to call, in what order, efficiency guidelines
5. **Rules** — naming conventions, deduplication, edge cases
6. **Output format** — exact structure expected

Keep under 500 words. Use dynamic instruction builders (not static strings).

### Interactive Chatbots [Chatbot]

Instructions define identity and principles only (~200 words). Do NOT put tool routing or research patterns in instructions.

```
Instructions: Identity + principles + behavioral guidelines
Tool descriptions: When and how to use each tool
User configuration: Domain specialization, constraints, formatting
```

### Key Rules [Both]

- NEVER pre-load content into instructions. Give a read tool + identifier instead.
- Guide tool usage explicitly — agents tend to over-use tools
- Use dynamic instruction builders, not static strings
- Pass data as JSON, not formatted markdown

## User-Configurable Settings [Chatbot]

Let users customize chatbot behavior without code changes. Three configuration types:

| Type | Purpose | Loaded When |
|------|---------|-------------|
| **Instruction** | Identity, behavior, domain focus | Always (system prompt) |
| **Rule** | Constraints, formatting, guardrails | Always (system prompt) |
| **Knowledge** | Reference docs, glossaries | On demand (via tool) |

Design principles:
- Instructions stay small (under 200 words). They anchor the persona.
- Rules are imperative and testable. "Always cite sources" not "try to cite sources."
- Knowledge can be large. Loaded on demand so it doesn't bloat the system prompt.
- Users can enable/disable individual entries without deleting them.
- Every instruction the chatbot receives should be visible and editable by the user. No hidden prompts.

### Storage: One File Per Config Entry

Store configs as individual markdown files in a structured folder hierarchy:

```
configs/
  instructions/
    identity-and-role.md
  rules/
    formatting-style.md
    citation-standards.md
  knowledge/
    domain-glossary.md
    methodology-guide.md
```

Each file is one config entry. The file contains the raw content the agent will receive. This mirrors how Claude Code stores its configuration: `CLAUDE.md` for instructions, `.claude/rules/*.md` for rules, each file is self-contained and independently editable.

Alternatively, if the application has a database and a UI, store configs as records (one row per entry) with fields: `name`, `type` (instruction/rule/knowledge), `content`, `enabled`, `order`. The principle is the same — one entry per concern, independently toggleable.

### How the Chatbot Accesses Configs

At runtime, the instruction builder collects enabled configs and assembles the system prompt:

```
build_instructions(context):
  1. Start with base identity (~50 words, hardcoded)
  2. Load all enabled "instruction" configs → append to system prompt
  3. Load all enabled "rule" configs → append to system prompt
  4. Return the assembled instruction string

  Knowledge configs are NOT loaded here.
  They are fetched on demand when the agent calls a knowledge tool.
```

The knowledge tool gives the agent access to reference material without bloating the system prompt:

```
Tool: get_project_knowledge
Description: "Retrieve project reference documents, glossaries, or methodology
             guides. Call this when you need domain context to answer accurately."
Parameters: name (str, optional) — specific doc name, or omit for all
Returns: JSON list of knowledge entries with name and content
```

The agent decides when it needs background material and calls this tool. Most questions don't need it, so the system prompt stays lean.

### Profile Templates

For common use cases, provide pre-built profiles (e.g., "Consultant", "Researcher", "Analyst") that bundle an instruction, rules, and skills.

Use **fork semantics**: copy template configs into the project as independent entries. After that, edits are project-scoped and don't affect the template.

## Progressive Disclosure [Chatbot]

Not all context should be loaded into the system prompt upfront.

| Tier | What | When Loaded |
|------|------|-------------|
| **Always** | Identity + behavioral rules + user instructions/rules | System prompt |
| **On demand** | Reference material, glossaries, domain definitions | Agent calls a knowledge tool |
| **Tool-level** | External data (database, APIs) | Each tool fetches its own data |

Why: system prompts have a budget. Every token of context dilutes the agent's focus on instructions.

## Streaming [Chatbot]

Stream responses token-by-token rather than waiting for the full response. Most SDKs make streaming and structured output mutually exclusive — for interactive chatbots, stream free text. Extract structured metadata (sources, reasoning) from tool call history after execution.

Set a `max_turns` limit (15 is reasonable) to prevent runaway tool loops.

## Source Tracking [Chatbot]

Track which sources the agent accessed programmatically at the tool level:

```
search() -> tracks all found documents
explore() -> tracks the explored document
read()    -> tracks the read document
```

Do NOT rely on the agent to cite correctly. Track sources from actual tool calls, not from generated text.

## Filter and Context Scoping [Chatbot]

When the chatbot serves a UI with filters (project, category, date range), inject these as context — not as tool parameters. Tools extract filters from context automatically. This keeps tool signatures stable and lets the agent focus on the question, not filter management.

## Data-Driven Configuration [Both]

Instead of one agent per use case, use one generic agent with runtime configs. Configs define what to extract, how to present, which types are enabled.

- Configs are stored in the database and editable from a UI
- Code constants serve as seed data only
- Adding a new use case = adding a new config, not writing new agent code
- The instruction builder reads configs from context to build dynamic sections

## Multi-Agent Patterns

Default to a single agent. Only split when:
1. **Context pollution** (>20 tools, conflicting instructions)
2. **Parallelization** (independent sub-tasks)
3. **Specialization** (fundamentally different capabilities)

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
7. **Put routing logic in instructions** — Tool descriptions carry the routing intelligence [Chatbot]
8. **Hidden instructions** — Users should be able to see and edit everything the chatbot receives [Chatbot]

## Checklists

### Processing Agent Checklist

- [ ] 3-5 tools (never more than 20)
- [ ] Dynamic instruction builder (not static string)
- [ ] Clear output schema (structured JSON)
- [ ] Model appropriate for the task
- [ ] Tools are read-only, return structured JSON
- [ ] Instructions under 500 words
- [ ] No pre-loaded content in instructions
- [ ] Data-driven configuration where possible

### Interactive Chatbot Checklist

- [ ] Instructions define identity and principles only (~200 words)
- [ ] Tool descriptions carry routing logic (not instructions)
- [ ] Think tool included for multi-tool agents
- [ ] User-configurable settings (instructions, rules, knowledge)
- [ ] Progressive disclosure (not everything in system prompt)
- [ ] Streaming with post-execution metadata extraction
- [ ] Source tracking at tool level (not agent-generated citations)
- [ ] Turn limit set (15 is reasonable)
- [ ] Filters injected as context, not tool parameters
- [ ] Profile templates with fork semantics
- [ ] All instructions visible and editable by the user
