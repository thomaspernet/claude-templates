---
name: design-agent
description: "Step-by-step agent creation workflow. Use when designing a new LLM-based agent."
---

# Design Agent

Follow these steps to design and implement a new agent.

## Step 1: Define the Goal

- What should this agent accomplish?
- What inputs does it receive?
- What output should it produce?
- Is this a new agent or should an existing agent be configured for this use case?

## Step 2: Select the Model

- Simple extraction/classification: small/fast model
- Complex reasoning or multi-step: large model
- Interactive chat with tools: reasoning model

## Step 3: Design the Tools

For each tool needed:
- Name it specifically (verb + noun: `search_notes`, `get_entity_values`)
- Make it read-only (no writes, no side effects)
- Return structured JSON
- Write a precise description (this is what the LLM uses to decide whether to call it)
- Keep total tool count to 3-5

## Step 4: Write the Instructions

Build a dynamic instruction function that takes context and returns a prompt string:
1. Role (one sentence)
2. Context (IDs, names — minimal)
3. Task (detailed — what to do, types, descriptions)
4. Tool usage (order, efficiency guidance)
5. Rules (naming, dedup, edge cases)
6. Output format (exact schema)

Keep under 500 words total.

## Step 5: Define the Output Schema

- Use structured output (Pydantic model or JSON schema)
- Prefer generic structures (dicts keyed by type) over hardcoded fields
- Include confidence scores or metadata if relevant

## Step 6: Test

- Test with representative inputs
- Verify tool selection (is it calling the right tools?)
- Verify output matches schema
- Test edge cases: empty input, large input, ambiguous input
- Check token usage — are instructions bloated?

## Checklist

- [ ] Clear goal and output defined
- [ ] Model selected for the task complexity
- [ ] 3-5 read-only tools with precise descriptions
- [ ] Dynamic instructions under 500 words
- [ ] Structured output schema
- [ ] Tested with representative and edge-case inputs
