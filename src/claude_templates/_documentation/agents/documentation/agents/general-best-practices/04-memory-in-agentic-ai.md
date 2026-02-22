# Memory in Agentic AI

> General best practices for designing memory systems in LLM-based agents. Not specific to any application or SDK. Based on research of Claude Code, OpenAI, LangChain/LangGraph, MemGPT/Letta, Cursor, and academic surveys (2024-2026).

---

## 1. The Memory Problem

LLM agents are stateless by default. Each API call receives a prompt, produces a response, and forgets everything. To build agents that reason across multiple turns, sessions, or tasks, memory must be explicitly designed.

The core tension: **context windows are finite, but useful information accumulates without bound.** Every memory system is ultimately a strategy for deciding what to keep, what to compress, and what to discard.

---

## 2. Memory Taxonomy

The academic consensus (from surveys like "Memory in the Age of AI Agents", 2025) identifies three types of agent memory:

| Type | Scope | Content | Lifetime |
|---|---|---|---|
| **Working memory** | Current task/turn | Plans, intermediate results, active reasoning | Within session |
| **Factual memory** | Cross-session | Facts, knowledge, user preferences | Persistent |
| **Experiential memory** | Cross-session | Past interactions, episodes, outcomes | Persistent |

These map to human cognitive science: working memory (what you're actively thinking about), semantic memory (facts you know), episodic memory (things you've experienced).

---

## 3. Context Window Management

The context window is the agent's "RAM." Everything the agent can reason about must fit inside it.

### Usage zones and degradation

| Usage | Quality | Action |
|---|---|---|
| 0-50% | Full precision | Normal operation |
| 50-70% | Beginning degradation | Consider compaction |
| 70-85% | Measurable precision loss | Compact now |
| 85%+ | Hallucination rate spikes | Output unreliable |

These thresholds are consistent across Claude, GPT-4, and Gemini models. The exact numbers vary by model, but the pattern holds: **quality degrades well before the context window is technically full.**

### Four strategies for managing context

From LangChain's "context engineering" framework:

1. **Writing**: Persist information outside the context window (scratchpads, files, databases)
2. **Selecting**: Pull only relevant information in (RAG, semantic search, tool selection)
3. **Compressing**: Retain essential tokens only (summarization, trimming)
4. **Isolating**: Partition context across multiple agents or state fields

Effective systems use all four. No single strategy is sufficient.

---

## 4. Working Memory Patterns

Working memory is the most critical layer for multi-turn agent interactions. It determines whether an agent can continue a task after interruptions.

### Pattern 1: Context window as working memory

The simplest approach. Everything the agent needs is in the prompt. No persistence mechanism.

- **Pro**: Zero overhead, no additional infrastructure
- **Con**: Lost between turns, lost on compaction, limited by context window
- **When to use**: Single-turn tasks, simple Q&A

### Pattern 2: Scratchpad / notepad tool

The agent has a tool to write structured notes to a persistent state object. The scratchpad is injected into the prompt on each turn.

- **Pro**: Survives across turns, agent controls what's saved
- **Con**: Consumes tokens on re-injection, agent may forget to save
- **When to use**: Multi-turn research, tasks with clarification loops
- **Used by**: Claude Code (subagent results), MemGPT (core memory), Digital Brain (working memory)

### Pattern 3: Automatic state extraction

The system automatically captures key state (plan progress, visited items, tool results) without the agent needing to explicitly save.

- **Pro**: Never forgets, no tool call overhead
- **Con**: May save too much or too little, no agent judgment
- **When to use**: As a fallback alongside Pattern 2

### Pattern 4: State object with selective exposure

The agent's runtime state has multiple typed fields. Only relevant fields are exposed to the LLM at each step.

- **Pro**: Prevents context pollution, fine-grained control
- **Con**: Complex to implement, requires careful schema design
- **When to use**: Agents with many parallel concerns

### Recommendation

**Use Pattern 2 (scratchpad tool) as the primary mechanism**, with Pattern 3 as a fallback for critical state. The agent has the best judgment about what matters -- automatic extraction either over-saves (wasting tokens) or under-saves (missing nuance).

---

## 5. Conversation History Management

### Trimming strategies

| Strategy | Mechanism | Tradeoff |
|---|---|---|
| **Keep all** | Full history in context | Expensive, degrades at high usage |
| **FIFO window** | Keep last N turns, drop older | Deterministic, loses older context |
| **Summary + recent** | Summarize older turns, keep recent verbatim | Best balance of cost and accuracy |
| **Token budget** | Keep as many recent turns as fit in a token limit | Adapts to message length |

The **summary + recent buffer** pattern is the industry standard. Claude Code, OpenAI Agents SDK, and LangChain all default to this approach.

### What survives compaction

When older messages are summarized, specific details are lost. The summary captures intent and outcomes but not:

- Exact error messages
- Specific function signatures
- Detailed architectural decisions
- Raw tool output

This is why working memory exists separately from conversation history: **the agent can control exactly what persists through compaction.**

---

## 6. Long-Term Memory Patterns

For information that should persist across sessions or conversations.

### Pattern 1: Curated files (CLAUDE.md pattern)

Human-curated markdown files loaded at session start. Versioned via Git.

- **Pro**: Predictable, controllable, no drift, version-controlled
- **Con**: Requires manual maintenance
- **Used by**: Claude Code (CLAUDE.md hierarchy), cursor rules

### Pattern 2: Automatic memory extraction

LLM-powered classifiers identify salient facts from conversations and store them automatically.

- **Pro**: No manual work, captures implicit preferences
- **Con**: Risk of storing noise, context leakage between topics
- **Used by**: ChatGPT (Saved Memories), Claude Code (auto-memory)

### Pattern 3: Vector store memory

Store facts as embeddings, retrieve by semantic similarity.

- **Pro**: Scales to large memory stores, semantic retrieval
- **Con**: Approximate matching, cannot answer relational queries
- **Used by**: AutoGPT, LangChain VectorStoreMemory

### Pattern 4: Knowledge graph memory

Build nodes and edges representing entities and relationships.

- **Pro**: Supports relational queries, captures structure
- **Con**: Complex to build and maintain
- **Used by**: Zep (Graphiti), Mem0g

### Emerging consensus

Use both unstructured (vector) for breadth and structured (graph) for depth. The most effective systems combine semantic retrieval with relational queries.

---

## 7. Industry Comparison

### Claude Code (the benchmark)

**Memory architecture:**
- **Persistent**: CLAUDE.md files (enterprise > user > project > directory rules). Loaded at session start. Git-versioned.
- **Auto-memory**: Automatically saves useful context (~200 lines, loaded per session).
- **Session**: Context window with compaction at 75-95% usage (varies by interface).
- **Isolation**: Subagents get fresh context windows -- work is delegated to prevent main context pollution.

**Compaction mechanism:**
1. Summary prompt injected as a user turn
2. Claude generates a structured summary
3. SDK replaces entire message history with summary
4. CLAUDE.md files re-loaded from disk (not summarized)

**Key insight**: Claude Code's strength is layered memory with clear boundaries. CLAUDE.md is the stable foundation, compaction manages session growth, and subagents prevent context pollution.

### OpenAI (ChatGPT + Agents SDK)

**ChatGPT:**
- Saved Memories (explicit facts, auto-updated from conversations)
- Referenced Chat History (RAG across all past conversations)
- Risk: context leakage between unrelated topics

**Agents SDK:**
- `TrimmingSession`: Keep last N user turns. Deterministic, zero overhead.
- `SummarizingSession`: Summary + recent buffer with configurable limits.
- No built-in long-term memory -- sessions are ephemeral.

### MemGPT / Letta

The most architecturally ambitious approach, inspired by OS virtual memory:

- **Main context (RAM)**: Fixed-size prompt with three partitions: static instructions, working context (scratchpad), FIFO message buffer.
- **External context (disk)**: Recall storage (searchable logs) + archival storage (vector DB).
- **Self-directed paging**: The LLM autonomously issues function calls to manage its own memory (`core_memory_append`, `archival_memory_search`, etc.).

**Tradeoff**: Memory management consumes reasoning tokens. The agent spends some of its capacity managing memory instead of solving the task.

### LangChain / LangGraph

Most extensive toolkit of memory primitives:

- `ConversationBufferMemory` -- keep all (short conversations)
- `ConversationSummaryBufferMemory` -- summary + buffer (best balance)
- `VectorStoreMemory` -- embed and retrieve by similarity
- `EntityMemory` -- track people, orgs, concepts
- `ConversationKnowledgeGraphMemory` -- build graph from conversation

LangGraph (2025) shifts to state-managed memory: short-term as agent state (checkpointed), long-term as separate memory store with namespaces.

### Cursor

- Tree-sitter parsing for code-aware chunking
- `@` mentions for explicit context injection
- Prompt rebuilt from scratch on every message
- Performance degrades at 80% context utilization
- Best practice: one task per session, break complex work into subtasks

---

## 8. Key Principles

### 1. Layer your memory

No single mechanism handles all needs. Use at least three layers:

- **Conversation history** (short-term): raw message pairs, managed by trimming/compaction
- **Working memory** (cross-turn): agent's scratchpad, structured notes, plans
- **Long-term knowledge** (cross-session): curated files, stored facts, learned preferences

### 2. Let the agent decide what to remember

Agent-writable scratchpads outperform automatic extraction. The agent has the best judgment about what's worth saving. Automatic extraction either over-saves (wasting tokens) or under-saves (missing nuance).

### 3. Set hard bounds

Without limits, memory grows unbounded. Use:
- Token/character limits on scratchpads
- Entry limits on long-term memory (e.g., 200 lines)
- Decay for low-relevance entries
- Deduplication and consolidation

### 4. Compact before it's too late

Quality degrades at 70-85% context usage, not at 100%. Compact proactively, not reactively.

### 5. Separate what the LLM sees from what's stored

Metadata, timestamps, and internal bookkeeping should not consume LLM tokens. Store full detail, inject summaries.

### 6. Use isolation for complex tasks

Delegate subtasks to subagents with fresh context windows. This prevents the main context from being polluted with task-specific details. The subagent returns only a summary.

### 7. Deterministic over probabilistic where possible

Summarization introduces variability. For reproducible results, prefer deterministic strategies (keep last N, structured extraction) and reserve LLM summarization for when compression is truly needed.

---

## 9. Common Pitfalls

| Pitfall | Description | Mitigation |
|---|---|---|
| **Context stuffing** | Loading everything into the prompt "just in case" | Select only what's relevant; use tools for on-demand loading |
| **Compaction amnesia** | Losing critical details during summarization | Working memory saves what matters separately from history |
| **Memory leakage** | Information from one topic bleeds into another | Scope memory to conversations/projects; clear between contexts |
| **Reasoning tax** | Agent spends tokens managing memory instead of solving tasks | Keep memory management simple; one tool, structured format |
| **Unbounded growth** | Memory grows forever, eventually degrading context | Hard limits, decay, deduplication |
| **Save-everything trap** | Storing every tool result "for later" | Only save synthesized findings, not raw data |

---

## Sources

- Claude Code memory docs (code.claude.com)
- "Memory in the Age of AI Agents" survey (arXiv:2512.13564, 2025)
- "Agentic Memory: Unified Long-Term and Short-Term" (arXiv:2601.01885, 2026)
- MemGPT: Towards LLMs as Operating Systems (arXiv:2310.08560)
- Mem0: Production-Ready AI Agents with Long-Term Memory (arXiv:2504.19413)
- OpenAI Agents SDK session memory cookbook
- LangGraph memory documentation
- LangChain "Context Engineering for Agents" blog
- Cursor context management analysis
- Zep temporal knowledge graph paper
