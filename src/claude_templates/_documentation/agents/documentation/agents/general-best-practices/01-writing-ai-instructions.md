# Writing Effective AI System Instructions

> General best practices for writing system prompts, instructions, rules, and skills for LLM-based chatbots. Not specific to any application.

---

## The Three Layers

Most configurable AI chatbot systems use three types of directives:

| Layer | Purpose | When Active |
|-------|---------|-------------|
| **Instruction** | Identity, role, tone, purpose | Always (system prompt) |
| **Rule** | Constraints, formatting, behavioral guardrails | Always (system prompt) |
| **Skill** | Analytical frameworks, domain methodologies | Always or on demand |

Instructions shape **who** the AI is. Rules shape **how** it behaves. Skills shape **what analytical tools** it applies.

---

## 1. Instructions (Identity and Role)

Instructions anchor all subsequent behavior. A well-defined identity makes every other directive more effective because the LLM has a clear persona to reason from.

### Structure

Follow this order:

1. **Role declaration**: One sentence defining the professional identity
2. **Purpose statement**: What the AI is designed to help the user accomplish
3. **Domain scope**: The specific area of expertise
4. **Engagement style**: Tone, depth calibration, how to interact
5. **Limitations clause**: What to do when knowledge is insufficient

### Examples

**Strong instruction:**
```
You are a Senior Management Consultant with deep expertise in strategy,
organizational design, and business transformation. Your purpose is to
help users analyze business problems, structure recommendations, and
develop actionable frameworks.

Engage the user as a trusted strategic advisor. Lead with conclusions,
support with evidence, and close with actionable next steps.

If a claim cannot be grounded in available information, state the
limitation explicitly. Ask one clarifying question when a request is
ambiguous rather than making assumptions.
```

**Weak instruction:**
```
You are a helpful assistant. Be friendly and informative.
```

The weak version provides no behavioral anchor. The LLM defaults to generic behavior.

### Principles

. **Specific beats generic.** "Senior Data Analyst specializing in trend analysis" outperforms "helpful AI assistant."
. **One concern per entry.** Separate role definition from domain context if both are long.
. **State the audience.** "You assist professionals in knowledge-intensive environments" shapes vocabulary automatically.
. **Include a fallback.** Tell the AI what to do when it doesn't know: "State uncertainty explicitly" or "Ask a clarifying question."
. **Under 200 words.** Longer instructions dilute focus. The LLM cannot weight 20 directives equally.

### Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| "You are a helpful assistant" | No behavioral anchor | Name a specific role and domain |
| Listing 10+ personality traits | LLM cannot weight all equally | Pick 3 core traits maximum |
| "Always be friendly and positive" | Vague modifier | "Engage the user as a capable professional" |
| Including tool usage procedures | Mixes identity with procedures | Keep instructions about who, not how |
| Pasting entire documents into the prompt | Bloats context, wastes tokens | Let the AI fetch content on demand |

---

## 2. Rules (Constraints and Formatting)

Rules define **what the AI must and must not do**. They are behavioral constraints applied to every response.

### Categories

| Category | Purpose | Example |
|----------|---------|---------|
| **Formatting** | Visual structure of responses | Bullet style, header usage, list types |
| **Accuracy** | How claims are sourced and qualified | Citation requirements, uncertainty language |
| **Scope** | What topics to address or avoid | Domain boundaries, redirect behavior |
| **Engagement** | Interaction patterns | No filler phrases, depth calibration |

### Examples

**Formatting rule:**
```
Use bullet points formatted with a dot (.) as the list marker. Do not
include the hyphen character (-) anywhere in your response.

Use headers to separate distinct sections in multi-part answers. Use
numbered lists only for sequential steps or ranked priorities.

Avoid restating the user's question before answering. Do not use filler
affirmations such as "Certainly!", "Great question!", or "Of course!".
```

**Accuracy rule:**
```
Always cite source documents by name when making claims. Distinguish
between what a source states directly and your interpretation.

If a fact or statistic cannot be verified from provided context, state
the limitation explicitly. Never fabricate citations, author names,
or statistics.

When multiple sources address the same topic, compare their findings
and note areas of agreement or contradiction.
```

### Writing Effective Rules

. **Imperative form.** "Always cite sources" is stronger than "You should try to cite sources."
. **Positive before negative.** Say what to do, then what not to do: "Use dot bullets. Do not use hyphens."
. **Specific and testable.** "Keep bullets to two sentences maximum" is enforceable. "Keep it brief" is not.
. **One category per entry.** Separate formatting from citation from scope rules. Mixing categories makes each weaker.
. **No contradictions.** If one rule says "be concise" and another says "provide detailed analysis," the LLM will oscillate between them.

### What NOT to Put in Rules

. Tool usage instructions (those belong in tool descriptions or separate procedure docs)
. Rigid response templates (reduces the AI's ability to adapt to different questions)
. Domain knowledge (belongs in skills or reference material)
. Personality traits (belongs in instructions)

---

## 3. Skills (Analytical Frameworks)

Skills give the AI **structured lenses** for analyzing questions. They transform a generic assistant into a domain specialist.

### Structure

Each skill entry should:

1. **Name the framework** clearly
2. **Define when to apply it**: Conditional triggers ("When asked for strategic analysis...")
3. **Describe the components**: Steps or elements of the framework
4. **Ground in evidence**: Reference available data, not general knowledge

### Examples

**Consulting frameworks:**
```
Apply these frameworks when relevant to the user's question:

Issue tree decomposition: Break complex problems into mutually exclusive,
collectively exhaustive (MECE) components before answering.

SWOT analysis: Identify Strengths, Weaknesses, Opportunities, and
Threats grounded in available evidence.

Stakeholder framing: Identify who is affected by a recommendation
and how when advising on decisions.

Prioritization: Apply impact vs. effort matrices or weighted scoring
when helping users prioritize actions.
```

**Research frameworks:**
```
Apply these frameworks when relevant to the user's question:

Systematic synthesis: Organize findings by theme, methodology, or
chronology rather than by individual document.

Research gap identification: Distinguish what is established from
what remains contested or unexplored.

Methodological critique: Evaluate study design, sample scope,
limitations, and generalizability when reviewing research.

Source evaluation: Assess currency, relevance, authority, accuracy,
and purpose of sources.
```

### Writing Effective Skills

. **Name frameworks explicitly.** "SWOT analysis" triggers structured behavior better than "analyze strategically."
. **Describe components.** Listing the four SWOT quadrants tells the AI exactly what to produce.
. **Keep it conditional.** "When asked for strategic analysis, apply..." triggers appropriately. "Always apply SWOT" is inappropriate for simple factual questions.
. **Ground in evidence.** Every framework should reference available data, not the AI's general training knowledge.

---

## 4. Composing a Full Profile

A profile bundles instructions, rules, and skills into a coherent persona. Design each layer to reinforce the others.

### Recommended Structure

| Entry | Layer | Purpose |
|-------|-------|---------|
| Identity and Role | Instruction | Who the AI is; primary behavioral anchor |
| Formatting Style | Rule | Visual structure of responses |
| Domain Constraints | Rule | Accuracy, citation, scope |
| Analytical Frameworks | Skill | Domain methodologies and lenses |

### Design Principles

. **Each profile serves a distinct persona.** A Consultant, Researcher, and Analyst have different priorities and communication styles.
. **Instructions define the persona; rules and skills specialize it.** The instruction says "you are a consultant." The rules say "lead with recommendations." The skills say "use MECE decomposition."
. **Shared rules across profiles.** Formatting rules can be identical. Domain rules differ.
. **Keep total prompt budget reasonable.** Aim for under 1000 words total across all entries. More dilutes each directive.

---

## 5. Testing and Debugging

### Verification Steps

1. Ask a question that exercises the role definition. Does the AI respond in character?
2. Ask for a list. Does it follow the formatting rule?
3. Ask an analytical question. Does it apply the specified frameworks?
4. Ask about something outside the provided data. Does it acknowledge the gap?

### Red Flags

. **AI ignores a rule**: Rule may be too vague, or contradicted by another entry
. **AI quotes instructions verbatim**: Instruction is too template-like; make it more principle-based
. **AI applies framework to every question**: Skill trigger is too broad; add conditional language
. **Responses are excessively long**: Too many rules/skills competing for attention; reduce total count
. **AI hedges constantly**: Too many accuracy/limitation rules stacking up; keep to one clear accuracy rule

---

## 6. General Principles

These apply regardless of which AI model or platform you use:

1. **The LLM reads directives as a flat priority list.** If you have 20 rules, the later ones get less weight. Front-load what matters most.
2. **Specificity wins.** "Use dot bullets, never hyphens" beats "format nicely."
3. **Shorter is stronger.** A 100-word instruction anchors behavior better than a 500-word one.
4. **Test with adversarial questions.** Ask edge cases: out-of-scope topics, ambiguous queries, requests to ignore rules.
5. **Iterate on one layer at a time.** Change the instruction, test. Then change a rule, test. Don't change everything at once.
6. **Separate concerns.** Identity in instructions, behavior in rules, methodology in skills. Mixing them weakens all three.

---

## Quick Reference Checklists

### Instruction Checklist
. [ ] Starts with a specific role declaration
. [ ] States the purpose and domain
. [ ] Defines engagement tone (2-3 adjectives)
. [ ] Includes a fallback for unknown information
. [ ] Under 200 words

### Rule Checklist
. [ ] Uses imperative form ("Always...", "Do not...")
. [ ] Is specific and testable
. [ ] Does not contradict other rules
. [ ] Covers one category per entry (formatting OR accuracy OR scope)
. [ ] Under 150 words per entry

### Skill Checklist
. [ ] Names frameworks explicitly
. [ ] Describes components or steps
. [ ] Specifies when to apply ("When asked for...")
. [ ] References available evidence, not general knowledge
. [ ] Under 200 words per entry
