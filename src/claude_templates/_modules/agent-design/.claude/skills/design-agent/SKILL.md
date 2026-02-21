---
name: design-agent
description: "Step-by-step agent creation workflow. Use when designing a new LLM-based agent."
---

# Design Agent

Follow these steps to design and implement a new agent.

## Step 1: Define the Goal and Archetype

- What should this agent accomplish?
- What inputs does it receive?
- What output should it produce?
- Is this a new agent or should an existing agent be configured for this use case?

Determine the archetype:

| Archetype | Output | Session | Example |
|-----------|--------|---------|---------|
| **Processing** | Structured JSON | Stateless (one run) | Extraction, classification, transformation |
| **Interactive chatbot** | Streamed free text | Stateful (conversation) | Research assistant, advisor, Q&A |

The archetype determines which patterns apply in subsequent steps.

For interactive chatbots, follow the **Claude Code architecture** — the reference model for chatbot agent design. Claude Code succeeds through: minimal principle-based instructions (~200 words), tool descriptions that carry routing logic, user-configurable settings (instructions/rules/knowledge mirroring CLAUDE.md/.claude/rules/skills), progressive disclosure, and a think tool for planning. See `agent-design.md` rules for the full explanation.

## Step 2: Select the Model

- Simple extraction/classification: small/fast model
- Complex reasoning or multi-step: large model
- Interactive chat with tools: reasoning model

## Step 3: Design the Tools

For each tool needed:
- Name it specifically (verb + noun: `search_notes`, `get_entity_values`)
- Make it read-only (no writes, no side effects)
- Return structured JSON
- Keep total tool count to 3-5 (processing) or 5-10 (chatbot)

### Tool descriptions carry routing logic

Write descriptions that explain **when** and **why** to use the tool, not just what it does:

```
Bad:    "Search the database"
OK:     "Search notes by keyword or semantic similarity"
Good:   "Find notes, entities, or insights by keyword or semantic search.
         Use target='notes' for documents, target='entities' for concepts,
         target='insights' for extracted findings."
```

For chatbots, never put routing logic in instructions. The agent reads all tool descriptions and picks the right tool based on the question.

### Complementary tool sets [Chatbot]

Design tools that cover different access patterns: overview (discover), search, navigate, read, detail, context. These compose naturally.

### Think tool [Chatbot]

Include a no-op scratchpad tool (`think(thought="...")`) for agents with >5 tools or multi-step reasoning. The agent calls it to reason before acting. It improves complex task performance by ~54%.

## Step 4: Write the Instructions

### Processing agents

Build a dynamic instruction function that takes context and returns a prompt string:
1. Role (one sentence)
2. Context (IDs, names — minimal)
3. Task (detailed — what to do, types, descriptions)
4. Tool usage (order, efficiency guidance)
5. Rules (naming, dedup, edge cases)
6. Output format (exact schema)

Keep under 500 words total.

### Interactive chatbots (Claude Code architecture)

Follow the Claude Code model: instructions define identity and principles only (~200 words). The rest is handled by other layers.

| Layer | Responsibility | Equivalent in Claude Code |
|-------|---------------|--------------------------|
| **Instructions** | Identity, principles, behavioral guidelines | `CLAUDE.md` |
| **Tool descriptions** | When and how to use each tool (routing logic) | Tool definitions |
| **User configuration** | Domain specialization, constraints, formatting | `.claude/rules/`, skills |

Instruction structure:
1. Role declaration (one sentence — specific role and domain)
2. Purpose statement (what the AI helps the user accomplish)
3. Engagement style (tone, depth calibration)
4. Limitations clause (what to do when knowledge is insufficient)

Do NOT include tool routing, research patterns, or step-by-step procedures. Tool descriptions handle routing. This is the core insight — the agent reasons from principles and picks tools based on their descriptions, not from scripts in the instructions.

## Step 5: Design User-Configurable Settings [Chatbot]

Let users customize behavior without code changes. Three configuration types:

| Type | Purpose | Loaded When |
|------|---------|-------------|
| **Instruction** | Identity, domain focus (~200 words) | Always (system prompt) |
| **Rule** | Constraints, formatting, guardrails | Always (system prompt) |
| **Knowledge** | Reference docs, glossaries | On demand (via tool) |

### Store configs as files: one file, one concern

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

Each markdown file is one config entry. The file content is what the agent receives. This mirrors Claude Code: `CLAUDE.md` = instruction, `.claude/rules/*.md` = rules, each independently editable. For apps with a database and UI, use records with `name`, `type`, `content`, `enabled`, `order` fields — same principle.

### Wire configs to the agent

The instruction builder collects enabled instruction and rule configs at startup:

```
build_instructions(context):
  1. Base identity (~50 words, hardcoded)
  2. Append all enabled instruction configs
  3. Append all enabled rule configs
  -> System prompt done. Knowledge is NOT loaded here.
```

Knowledge configs are served by a dedicated tool the agent calls on demand:

```
Tool: get_project_knowledge
Description: "Retrieve project reference docs, glossaries, or guides.
             Call when you need domain context to answer accurately."
Returns: JSON list of knowledge entries { name, content }
```

Most questions don't need knowledge, so the system prompt stays lean. The agent decides when it needs background material.

### Design principles

- Rules are imperative and testable: "Always cite sources" not "try to cite sources"
- Knowledge loads on demand (doesn't bloat system prompt)
- Users can enable/disable entries without deleting them
- Every instruction the chatbot receives should be visible and editable

### Profile templates

For common use cases, provide pre-built profiles that bundle instruction, rules, and skills. Apply with **fork semantics**: copy templates as independent entries. Edits are project-scoped and don't affect the template.

## Step 6: Define the Output

### Processing agents

- Use structured output (Pydantic model or JSON schema)
- Prefer generic structures (dicts keyed by type) over hardcoded fields
- Include confidence scores or metadata if relevant

### Interactive chatbots

- Stream free text (most SDKs make streaming and structured output mutually exclusive)
- Extract structured metadata (sources, reasoning) from tool call history after execution
- Track sources programmatically at the tool level, not from generated text
- Set a `max_turns` limit (15 is reasonable) to prevent runaway tool loops

## Step 7: Handle Context and Filters [Chatbot]

- Load conversation history so the agent can reference previous exchanges
- Inject UI filters (project, category, date range) as agent context, not tool parameters
- Use progressive disclosure: identity + rules always loaded; reference material on demand via tool

## Step 8: Test

- Test with representative inputs
- Verify tool selection (is it calling the right tools?)
- Verify output matches schema (processing) or follows rules (chatbot)
- Test edge cases: empty input, large input, ambiguous input
- Check token usage — are instructions bloated?
- [Chatbot] Test that user-configurable settings (instructions, rules, skills) actually change behavior
- [Chatbot] Verify source tracking matches actual tool calls
- [Chatbot] Test streaming end-to-end

## Checklists

### Processing Agent

- [ ] Clear goal and structured output defined
- [ ] Model selected for the task complexity
- [ ] 3-5 read-only tools with precise descriptions
- [ ] Dynamic instructions under 500 words
- [ ] Structured output schema (generic, keyed by type)
- [ ] Data-driven configuration where possible
- [ ] Tested with representative and edge-case inputs

### Interactive Chatbot

- [ ] Identity-focused instructions (~200 words)
- [ ] Tool descriptions carry routing logic (not instructions)
- [ ] Think tool included for multi-tool agents
- [ ] User-configurable settings (instructions, rules, knowledge)
- [ ] Profile templates with fork semantics
- [ ] Progressive disclosure (not everything in system prompt)
- [ ] Streaming with post-execution metadata extraction
- [ ] Source tracking at tool level
- [ ] Turn limit set (15 is reasonable)
- [ ] Filters injected as context, not tool parameters
- [ ] All instructions visible and editable by the user
- [ ] Tested with user config changes, edge cases, and streaming
