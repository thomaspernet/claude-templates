# Chatbot and Tool Patterns

> General best practices for building LLM-based chatbots with tool use. Covers architecture patterns for interactive agents that navigate data, use tools, and stream responses. Not specific to any application.

---

## 1. Architecture: Instructions vs Tool Descriptions

The most common mistake in chatbot design is putting tool routing logic into instructions. Instead, separate concerns:

| Layer | Responsibility | Example |
|-------|---------------|---------|
| **Instructions** | Identity, principles, behavioral guidelines | "Think before acting. Cite sources. Admit gaps." |
| **Tool descriptions** | When and how to use each tool | "Search the knowledge base by keyword or semantic similarity" |
| **User configuration** | Domain specialization, constraints | "Focus on biomedical research. Always cite publication year." |

Instructions should never say "when the user asks X, call tool Y." The agent reads all tool descriptions and picks the right tool based on the question. This is more flexible because:
- New tools automatically become available without instruction changes
- The agent adapts to novel question types
- Tool descriptions are maintained alongside tool code

---

## 2. The Think Tool

A think tool is a no-op scratchpad: the agent calls `think(thought="...")` to reason before acting. The thought is stored in the tool call history and visible to the agent's context, but produces no output for the user.

### Why It Works

- Forces the agent to plan before calling tools (reduces wasted calls)
- Makes reasoning visible in logs for debugging
- Anthropic's research shows think tools improve complex task performance by ~54%

### Design

```
Name: think
Parameters: thought (str) -- The agent's internal reasoning
Returns: Empty string (no-op)
Side effects: None
```

The tool does nothing. Its value is that calling it forces the agent to articulate its plan in a structured way that becomes part of its context window.

### When to Include

Include the think tool for any agent that:
- Has more than 5 tools to choose from
- Handles multi-step reasoning (research, analysis)
- Needs to plan a strategy before executing

Skip it for simple agents with 1-2 tools where the action is obvious.

---

## 3. Tool-Driven Routing

Each tool's description is the primary mechanism for routing agent behavior. Write descriptions that explain **when** and **why** to use the tool, not just what it does.

### Description Quality Spectrum

```
Bad:    "Search the database"
OK:     "Search notes by keyword or semantic similarity"
Good:   "Find notes, entities, or insights by keyword or semantic search.
         Use target='notes' for documents, target='entities' for concepts
         like topics or methodologies, target='insights' for extracted
         findings like summaries or key points."
```

The good description tells the agent:
- What targets are available
- When to use each target
- What kind of results to expect

### Complementary Tool Sets

Design tools that cover different access patterns. A typical knowledge-base chatbot needs:

| Pattern | Tool | Purpose |
|---------|------|---------|
| **Overview** | discover | What exists? (counts, categories, types) |
| **Search** | search | Find by content (keyword or semantic) |
| **Navigate** | explore | See connections from a node |
| **Read** | read | Get actual content |
| **Detail** | get_insights, get_entities, etc. | Specific metadata about a node |
| **Context** | fetch_history | Previous conversation actions |

These compose naturally: discover -> search -> explore -> read -> get_details.

---

## 4. Progressive Disclosure

Not all context should be loaded into the system prompt upfront. Use a layered approach:

### Loading Tiers

| Tier | What | When Loaded | Example |
|------|------|-------------|---------|
| **Always** | Identity + behavioral rules | System prompt | "You are a research assistant. Cite sources." |
| **Always** | User instructions + constraints | System prompt | Custom rules from project settings |
| **On demand** | Reference material, glossaries | Agent calls a tool | Knowledge docs, domain definitions |
| **Tool-level** | Data from external sources | Each tool fetches its own data | Database queries, API calls |

### Why This Matters

- System prompts have a budget. Every token of context dilutes the agent's focus on instructions.
- Reference material (glossaries, methodology guides) is only relevant to some questions.
- An on-demand knowledge tool lets the agent decide when it needs background material.

### The Knowledge Tool Pattern

Provide a tool that retrieves user-defined reference material:

```
Name: get_reference_docs
Description: "Retrieve user-defined reference documents and project knowledge.
              Call this when you need domain definitions, glossaries, or
              methodology guides to answer accurately."
Parameters: name (str, optional) -- specific doc name, or omit for all
Returns: JSON with reference document contents
```

The agent calls this tool when it encounters domain-specific terminology or needs background context, rather than having all reference material in the system prompt.

---

## 5. User-Configurable Settings

Let users customize chatbot behavior without code changes. Three configuration types cover most needs:

| Type | Purpose | Loaded When | Example |
|------|---------|-------------|---------|
| **Instruction** | Identity, behavior, domain focus | Always (system prompt) | "Focus on methodology and evidence quality" |
| **Rule** | Constraints, formatting, guardrails | Always (system prompt) | "Always cite publication year. Never speculate." |
| **Knowledge** | Reference docs, glossaries, context | On demand (via tool) | "Glossary of biomedical terms" |

### Design Principles

- **Instructions** stay small (under 200 words). They anchor the persona.
- **Rules** are imperative and testable. "Always cite sources" not "try to cite sources."
- **Knowledge** can be large. It's loaded on demand so it doesn't bloat the system prompt.
- Users can enable/disable individual entries without deleting them.
- Order matters: entries are injected in user-defined order.

### Profile Templates

For common use cases, provide pre-built profiles (e.g., "Consultant", "Researcher", "Analyst") that bundle an instruction, rules, and skills. Users select a profile as a starting point, then customize.

Profile application should use **fork semantics**: copy template configs into the project as independent entries. After that, edits are project-scoped and don't affect the template.

---

## 6. Streaming

Interactive chatbots should stream responses token-by-token rather than waiting for the full response.

### Architecture

```
User sends message
  -> Build agent context (filters, history, configs)
  -> Execute agent with streaming enabled
  -> Text deltas streamed as events (SSE, WebSocket, etc.)
  -> After completion: extract structured metadata (sources, reasoning)
```

### Key Constraint

Most LLM SDKs make streaming and structured output mutually exclusive. The agent either:
- **Streams free text** (good for user experience)
- **Returns structured JSON** (good for programmatic use)

For interactive chatbots, stream free text. Extract structured data (sources, confidence, reasoning steps) from the agent's context or tool call history after execution, not from the output itself.

### Turn Limits

Set a `max_turns` limit to prevent runaway tool loops. A typical research flow uses 5-8 turns:

```
Turn 1: think (plan approach)
Turn 2: search (find relevant documents)
Turn 3: explore (see connections)
Turn 4-5: read (get content)
Turn 6-7: get details (insights, entities)
Turn 8: Final answer
```

15 turns is a reasonable ceiling for interactive chatbots. Too generous = user waits too long. Too strict = agent can't complete complex research.

---

## 7. Source Tracking

When a chatbot references documents, track which sources it accessed for attribution.

### Pattern

Every tool that touches a document should register it as a source:

```
search() -> tracks all found documents
explore() -> tracks the explored document
read() -> tracks the read document
```

Populate a source list on the agent context. After execution, deduplicate and return sources alongside the answer.

### Why Not Let the Agent Cite?

Agents can hallucinate citations. Instead:
- Track sources programmatically (tool-level, not agent-level)
- The agent's answer references documents naturally ("According to Document X...")
- The source list is verified from actual tool calls, not generated text

---

## 8. Conversation History

### Session Management

Load prior conversation messages into the agent's context so it can reference previous exchanges. The LLM SDK typically handles this as a message list.

### Structured History Access

For complex conversations, provide a tool that gives structured access to previous actions:

```
Name: fetch_previous_reasoning
Description: "Fetch previous tool calls and findings from this conversation."
Parameters: limit (int, optional) -- Number of previous sessions
Returns: Structured summary of previous actions, documents explored, conclusions
```

This is more useful than raw message history because:
- The agent can see what it already explored (avoids re-searching)
- Previous conclusions are summarized, not buried in long messages
- Tool call details (which documents, which searches) are structured

---

## 9. Filter and Context Scoping

When the chatbot serves a UI with filters (project, category, date range, etc.), inject these as context rather than tool parameters.

### Pattern

```
Frontend sends: { filters: { project: "uuid", tags: ["research"], type: ["pdf"] } }
Backend injects: filters into AgentContext
Tools extract: filters from context automatically
Result: All tool calls respect active filters without the agent managing them
```

### Why Context, Not Parameters

- The agent doesn't need to understand filter mechanics
- Filters change per-request; tool signatures stay stable
- Adding new filter dimensions doesn't require changing tool interfaces
- The agent focuses on the question, not on filter management

---

## Quick Reference

### Chatbot Architecture Checklist

- [ ] Instructions define identity and principles (under 200 words)
- [ ] Tool descriptions carry routing logic (not instructions)
- [ ] Think tool included for multi-tool agents
- [ ] User-configurable settings (instructions, rules, knowledge)
- [ ] Progressive disclosure (not everything in system prompt)
- [ ] Streaming with post-execution metadata extraction
- [ ] Source tracking at tool level (not agent-generated citations)
- [ ] Conversation history available via structured tool
- [ ] Turn limit set (15 is a reasonable ceiling)
- [ ] Filters injected as context, not tool parameters
