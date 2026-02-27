---
name: review-changes
description: "Pre-commit code review covering architecture, quality, security, and correctness."
---

# Review Changes

## When to Use

**Perfect for:**
- Before every commit, especially when touching multiple layers
- After a significant refactor to catch regressions
- When changes span backend and frontend

**Not ideal for:**
- Post-merge retrospectives
- Architecture redesign discussions
- Reviewing code you didn't write (use a dedicated code review process instead)

---

> **Core Philosophy:** Review is a gate, not a suggestion. A finding in any category means fixing before committing — not logging a TODO and moving on.

## ⚠️ CRITICAL

1. **Layer violations block the commit.** DB queries outside `infrastructure/`, business logic in API endpoints, or domain models importing from services — these are architecture violations, not style issues. Fix before proceeding.
2. **Secrets never get committed.** If a hardcoded credential, API key, or password is found anywhere in the diff, stop and remove it before anything else.

---

## 1. Architecture Check

- [ ] No business logic in API endpoints
- [ ] No DB queries outside `infrastructure/`
- [ ] Services don't import from API layer
- [ ] Domain models don't import from other layers
- [ ] Dependency injection used (no hard-coded dependencies)

## 2. Code Quality

- [ ] Type hints on all new/modified functions
- [ ] No magic strings — constants or enums used
- [ ] No `any` types in TypeScript
- [ ] Early returns instead of deep nesting
- [ ] No debugging code left in (`print`, `console.log`, `debugger`)

## 3. Async / Concurrency

- [ ] All async operations awaited
- [ ] `useEffect` has cleanup function for async work
- [ ] `AbortController` used for fetch in React effects
- [ ] No shared DB connections between concurrent tasks

## 4. Security

- [ ] No hardcoded secrets or credentials
- [ ] No SQL/Cypher injection vulnerabilities
- [ ] User input validated before processing
- [ ] Error messages don't leak internal details

## 5. Testing

- [ ] New functionality has tests
- [ ] Existing tests still pass
- [ ] Edge cases covered (empty input, null, errors)

## Output

Report findings with file path and line number, grouped by category:

```
[ARCHITECTURE] backend/api/routers/entity.py:42
  Issue: DB query found outside infrastructure layer
  Fix:   Move to infrastructure/repositories/entity_repo.py

[SECURITY] backend/services/auth.py:17
  Issue: Hardcoded API key
  Fix:   Load from environment variable
```

Conclude with: **Approved** (no blockers) or **Changes required** (list all blockers).
