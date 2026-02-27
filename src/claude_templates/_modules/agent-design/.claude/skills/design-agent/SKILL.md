---
name: design-agent
description: "Use this skill when designing or building a new LLM-based agent. Invoke when the user mentions building an AI agent, choosing between a processing agent and a chatbot, designing tools for an LLM, or structuring system instructions — even if they haven't settled on an architecture yet."
---

# Design Agent

## When to Use

**Perfect for:**
- Designing a new LLM-based agent from scratch
- Choosing between a processing agent and an interactive chatbot
- Structuring tools, instructions, and user-configurable settings

**Not ideal for:**
- Modifying a single tool or prompt in an existing agent (edit directly)
- Debugging a misbehaving agent (use a dedicated diagnostic session)
- Prompt-only tasks with no tool use

---

> **Core Philosophy:** An agent's intelligence comes from clear tool descriptions and minimal instructions — not from lengthy scripts. Instructions define identity; tool descriptions carry routing logic. The simpler the system prompt, the more reliably the model reasons.

## ⚠️ CRITICAL

1. **Never put routing logic in instructions.** Tool descriptions tell the agent when and why to use each tool. Instructions that say "if the user asks X, call tool Y" will degrade as the model ages. Write tool descriptions that make routing self-evident.
2. **Read-only tools only.** Tools must not write, delete, or have side effects unless explicitly required and confirmed by the user. Mutations belong in services called by tools — not in the tools themselves.
3. **Stay under the token budget.** Processing agent instructions: under 500 words. Chatbot instructions: under 200 words. Every sentence that doesn't change behavior should be cut.

---

## Step 1: Define the Goal and Archetype

- What should this agent accomplish?
- What inputs does it receive and what output does it produce?
- Is this a new agent or should an existing one be configured for this use case?

Determine the archetype:

| Archetype | Output | Session | Example |
|-----------|--------|---------|---------|
| **Processing** | Structured JSON | Stateless (one run) | Extraction, classification, transformation |
| **Interactive chatbot** | Streamed free text | Stateful (conversation) | Research assistant, advisor, Q&A |

The archetype determines which patterns apply in subsequent steps. For interactive chatbots, follow the **Claude Code architecture** — the reference model for chatbot design: minimal principle-based instructions (~200 words), tool descriptions that carry routing logic, user-configurable settings (instructions / rules / knowledge), progressive disclosure, and a think tool for planning.

## Step 2: Select the Model

- Simple extraction/classification → small/fast model
- Complex reasoning or multi-step → large model
- Interactive chat with tools → reasoning model

## Step 3: Design the Tools

For each tool:
- Name it specifically (verb + noun: `search_notes`, `get_entity_values`)
- Make it read-only (no writes, no side effects)
- Return structured JSON
- Keep total count to 3–5 (processing) or 5–10 (chatbot)

Write descriptions that explain **when** and **why** to use the tool:

```
Bad:    "Search the database"
OK:     "Search notes by keyword or semantic similarity"
Good:   "Find notes, entities, or insights by keyword or semantic search.
         Use target='notes' for documents, target='entities' for concepts,
         target='insights' for extracted findings."
```

**Chatbot:** Design complementary tool sets covering different access patterns: overview (discover), search, navigate, read, detail, context.

**Think tool:** Include a no-op scratchpad tool (`think(thought="...")`) for agents with >5 tools or multi-step reasoning. It improves complex task performance by ~54%.

## Step 4: Write the Instructions

### Processing agents

Dynamic instruction function → takes context → returns a prompt string:
1. Role (one sentence)
2. Context (IDs, names — minimal)
3. Task (detailed — what to do, types, edge cases)
4. Tool usage (order, efficiency guidance)
5. Rules (naming, dedup, edge cases)
6. Output format (exact schema)

Keep under 500 words total.

### Interactive chatbots (Claude Code architecture)

Instructions define identity and principles only (~200 words):

| Layer | Responsibility | Equivalent in Claude Code |
|-------|---------------|--------------------------|
| **Instructions** | Identity, principles, behavioral guidelines | `CLAUDE.md` |
| **Tool descriptions** | Routing logic — when and why to use each tool | Tool definitions |
| **User configuration** | Domain specialization, constraints, formatting | `.claude/rules/`, skills |

Instruction structure:
1. Role declaration (one sentence)
2. Purpose (what the AI helps the user accomplish)
3. Engagement style (tone, depth calibration)
4. Limitations clause (what to do when knowledge is insufficient)

## Step 5: Design User-Configurable Settings [Chatbot]

| Type | Purpose | Loaded When |
|------|---------|-------------|
| **Instruction** | Identity, domain focus (~200 words) | Always (system prompt) |
| **Rule** | Constraints, formatting, guardrails | Always (system prompt) |
| **Knowledge** | Reference docs, glossaries | On demand (via tool) |

Store configs as files — one file, one concern:

```
configs/
  instructions/
    identity-and-role.md        # "You are a Senior Consultant..."
  rules/
    formatting-style.md         # "Use dot bullets. No hyphens."
    citation-standards.md       # "Always cite sources by name."
  knowledge/
    domain-glossary.md          # Loaded on demand by the agent
    methodology-guide.md
```

The instruction builder collects enabled instruction and rule configs at startup. Knowledge is served via a dedicated tool the agent calls on demand — most questions don't need it, so the system prompt stays lean.

## Step 6: Define the Output

**Processing agents:** Structured output (Pydantic model or JSON schema). Prefer generic structures (dicts keyed by type) over hardcoded fields.

**Interactive chatbots:** Stream free text. Extract structured metadata (sources, reasoning) from tool call history after execution — never parse it from generated text. Set `max_turns` limit (15 is reasonable).

## Step 7: Handle Context and Filters [Chatbot]

- Load conversation history so the agent can reference previous exchanges
- Inject UI filters (project, category, date range) as agent context, not tool parameters
- Progressive disclosure: identity + rules always loaded; reference material on demand

## Step 8: Test

- Test with representative inputs — does the agent call the right tools?
- Verify output matches schema (processing) or follows rules (chatbot)
- Test edge cases: empty input, large input, ambiguous input
- Check token usage — are instructions bloated?
- [Chatbot] Test that user-configurable settings actually change behavior
- [Chatbot] Verify source tracking matches actual tool calls
- [Chatbot] Test streaming end-to-end

## Output

Report the design decisions before writing any code:

```
## Agent Design: {Name}

Archetype:    Processing | Interactive Chatbot
Model:        {model rationale}

Tools ({n}):
  - {tool_name}: {when/why description}
  - {tool_name}: {when/why description}

Instructions: {word count} words
  Layers: Identity / Rules / Knowledge (on-demand)

Output:
  - {schema or stream description}

User config:  {instruction files} / {rule files} / {knowledge files}
```

## Checklists

### Processing Agent

- [ ] Clear goal and structured output defined
- [ ] Model selected for the task complexity
- [ ] 3–5 read-only tools with routing logic in descriptions
- [ ] Dynamic instructions under 500 words
- [ ] Structured output schema (generic, keyed by type)
- [ ] Tested with representative and edge-case inputs

### Interactive Chatbot

- [ ] Identity-focused instructions (~200 words)
- [ ] Tool descriptions carry routing logic (not instructions)
- [ ] Think tool included for multi-tool agents
- [ ] User-configurable settings (instructions, rules, knowledge)
- [ ] Progressive disclosure (not everything in system prompt)
- [ ] Streaming with post-execution metadata extraction
- [ ] Source tracking at tool level, not from generated text
- [ ] Turn limit set (15 is reasonable)
- [ ] Filters injected as context, not tool parameters
- [ ] All instructions visible and editable by the user
- [ ] Tested with user config changes, edge cases, and streaming
