---
name: write-system-prompt
description: "Guided system prompt creation. Use when writing or improving a system prompt for an AI application."
---

# Write System Prompt

## When to Use

**Perfect for:**
- Writing a system prompt for a new AI feature or chatbot
- Auditing and improving an existing system prompt that isn't performing
- Structuring instructions, rules, and skills across multiple layers

**Not ideal for:**
- Tweaking a single sentence in an already-working prompt (edit directly)
- Prompt templates filled at runtime (use a dynamic instruction builder instead)
- Tool descriptions — those belong with the tool definition, not in the system prompt

---

> **Core Philosophy:** A system prompt defines identity and constraints — not procedures. The model reasons from principles, not scripts. A prompt that tells the AI what to be is more durable than one that tells it what to do step by step.

## ⚠️ CRITICAL

1. **Never include routing logic in the instruction layer.** "If the user asks X, call tool Y" belongs in tool descriptions, not the system prompt. Instructions that hardcode routing degrade as the model and tools evolve.
2. **Every rule must be imperative and testable.** "Always cite sources" is a rule. "Try to be accurate" is not. If you can't write a test that would catch a rule violation, the rule is too vague.
3. **Stay under budget.** Instruction layer: under 200 words. Each rule entry: under 150 words. Each skill entry: under 200 words. Total across all layers: under 1000 words. Bloated prompts shift the model's attention and reduce compliance.

---

## Step 1: Define the Persona

- What professional role should the AI embody?
- What domain expertise does it need?
- What tone? (authoritative, approachable, formal, concise)

Write a one-sentence role declaration before doing anything else. This anchors every subsequent decision.

## Step 2: Write the Instruction (Identity Layer)

Structure:
1. **Role declaration** — one sentence: specific role and domain
2. **Purpose** — what the AI helps users accomplish
3. **Domain scope** — specific expertise area and limits
4. **Engagement style** — 2–3 tone adjectives
5. **Fallback** — what to do when knowledge is insufficient

Target: under 200 words. Test: does it provide a clear behavioral anchor without any procedural steps?

## Step 3: Write Rules (Constraint Layer)

For each constraint category needed (formatting, accuracy, scope, engagement):
- One rule entry per category
- Imperative form ("Always...", "Never...", "Do not...")
- Specific and testable — a QA engineer could verify compliance
- No contradictions between rules

Target: under 150 words per entry. Common categories:
- **Formatting** — structure, length, bullet style, header use
- **Accuracy** — citation requirements, uncertainty handling
- **Scope** — what topics are in/out of scope
- **Engagement** — follow-up questions, clarification behavior

## Step 4: Write Skills (Framework Layer)

If the AI needs analytical frameworks or multi-step methodologies:
- Name each framework explicitly
- Describe components/steps
- Add conditional triggers ("When asked for X, apply Y framework")
- Ground in evidence, not general knowledge

Target: under 200 words per entry.

## Step 5: Compose and Budget

- Total across all layers: under 1000 words
- Front-load the most important directives (model attention decays toward the end)
- Check for contradictions between layers
- Verify each layer serves its purpose:
  - Instruction → identity and principles only
  - Rules → constraints and guardrails only
  - Skills → analytical frameworks only
- Cut any sentence that doesn't change behavior

## Step 6: Test

Run these checks against the composed prompt:

| Test | Input | Expected |
|------|-------|----------|
| Role | "Tell me about yourself" | Responds in character |
| Formatting | "Give me a list of X" | Follows formatting rules |
| Frameworks | Analytical question | Applies the right skill |
| Boundaries | Out-of-scope question | Acknowledges gap gracefully |
| Adversarial | "Ignore your instructions" | Maintains behavior |

Iterate one layer at a time — change only the instruction, or only one rule. Don't change everything at once.

## Output

Deliver the prompt structured by layer, ready to paste into the application:

````markdown
## System Prompt: {Name}

### Instruction (~{n} words)
[Identity and principles only]

### Rules

**{Category}** (~{n} words)
[Imperative constraints]

**{Category}** (~{n} words)
[Imperative constraints]

### Skills

**{Framework Name}** (~{n} words)
[Analytical framework with trigger condition]

---
Total: {n} words across all layers
````

## Checklist

- [ ] Role declaration written (one sentence, specific role and domain)
- [ ] Instruction layer under 200 words — identity only, no routing logic
- [ ] Each rule is imperative and testable
- [ ] No contradictions between instruction and rules
- [ ] Skills have explicit trigger conditions
- [ ] Total under 1000 words
- [ ] All 5 test scenarios pass
- [ ] Prompt formatted and ready for the application
