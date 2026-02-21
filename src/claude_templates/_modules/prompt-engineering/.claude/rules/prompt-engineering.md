# Prompt Engineering Best Practices

## The Three Layers

| Layer | Purpose | When Active |
|-------|---------|-------------|
| **Instruction** | Identity, role, tone, purpose | Always (system prompt) |
| **Rule** | Constraints, formatting, behavioral guardrails | Always (system prompt) |
| **Skill** | Analytical frameworks, domain methodologies | Always or on demand |

Instructions shape **who** the AI is. Rules shape **how** it behaves. Skills shape **what analytical tools** it applies.

## Writing Instructions (Identity Layer)

Structure in this order:
1. **Role declaration** — one sentence defining professional identity
2. **Purpose statement** — what the AI helps accomplish
3. **Domain scope** — specific area of expertise
4. **Engagement style** — tone, depth calibration
5. **Limitations clause** — what to do when knowledge is insufficient

### Strong vs Weak

```
Strong: "You are a Senior Data Analyst specializing in trend analysis.
        Help users interpret datasets, identify patterns, and build
        actionable recommendations. Lead with findings, support with
        methodology. State uncertainty explicitly."

Weak:   "You are a helpful assistant. Be friendly and informative."
```

### Principles

- Specific beats generic. "Senior Data Analyst" > "helpful assistant"
- Under 200 words — longer instructions dilute focus
- Include a fallback for unknown information
- Maximum 3 personality traits — LLM cannot weight 20 equally

## Writing Rules (Constraint Layer)

Categories: Formatting | Accuracy | Scope | Engagement

### Principles

- **Imperative form**: "Always cite sources" > "You should try to cite sources"
- **Positive before negative**: say what to do, then what not to do
- **Specific and testable**: "Max 2 sentences per bullet" > "Keep it brief"
- **One category per entry**: don't mix formatting with citation rules
- **No contradictions**: "be concise" + "provide detailed analysis" = oscillation
- Under 150 words per rule entry

### Do NOT put in rules

- Tool usage instructions (belong in tool descriptions)
- Rigid response templates (reduces adaptability)
- Domain knowledge (belongs in skills)
- Personality traits (belongs in instructions)

## Writing Skills (Framework Layer)

- **Name frameworks explicitly**: "SWOT analysis" triggers better than "analyze strategically"
- **Describe components**: listing SWOT quadrants tells the AI what to produce
- **Keep conditional**: "When asked for strategic analysis, apply..." not "Always apply SWOT"
- **Ground in evidence**: reference available data, not general training knowledge
- Under 200 words per skill entry

## Testing Prompts

1. Ask a question that exercises the role. Does it respond in character?
2. Ask for a list. Does it follow formatting rules?
3. Ask an analytical question. Does it apply the frameworks?
4. Ask about something outside scope. Does it acknowledge the gap?

### Red Flags

- AI ignores a rule: too vague or contradicted by another
- AI quotes instructions verbatim: too template-like, make it principle-based
- AI applies framework to every question: trigger too broad, add conditionals
- Responses excessively long: too many rules competing, reduce count

## Budget

- Instructions: under 200 words
- Each rule entry: under 150 words
- Each skill entry: under 200 words
- Total system prompt: under 1000 words
- Front-load what matters most — later directives get less weight
