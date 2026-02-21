---
name: write-system-prompt
description: "Guided system prompt creation. Use when writing or improving a system prompt for an AI application."
---

# Write System Prompt

Follow these steps to create an effective system prompt.

## Step 1: Define the Persona

- What professional role should the AI embody?
- What domain expertise does it need?
- What tone? (e.g., authoritative, approachable, formal)
- Write a one-sentence role declaration

## Step 2: Write the Instruction (Identity)

Following this structure:
1. Role declaration (one sentence)
2. Purpose — what the AI helps users accomplish
3. Domain scope — specific expertise area
4. Engagement style — 2-3 tone adjectives
5. Fallback — what to do when uncertain

Target: under 200 words. Test: does it provide a clear behavioral anchor?

## Step 3: Write Rules (Constraints)

For each category needed (formatting, accuracy, scope, engagement):
- One rule entry per category
- Imperative form ("Always...", "Do not...")
- Specific and testable
- No contradictions between rules

Target: under 150 words per entry.

## Step 4: Write Skills (Frameworks)

If the AI needs analytical frameworks:
- Name each framework explicitly
- Describe components/steps
- Add conditional triggers ("When asked for...")
- Ground in evidence, not general knowledge

Target: under 200 words per entry.

## Step 5: Compose and Budget

- Total across all layers: under 1000 words
- Front-load the most important directives
- Check for contradictions between layers
- Verify each layer serves its purpose (identity / constraints / methodology)

## Step 6: Test

Run these checks:
1. Role: "Tell me about yourself" — responds in character?
2. Formatting: "Give me a list" — follows rules?
3. Frameworks: analytical question — applies skills?
4. Boundaries: out-of-scope question — acknowledges gap?
5. Adversarial: "Ignore your instructions" — maintains behavior?

Iterate one layer at a time. Don't change everything at once.
