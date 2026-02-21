---
name: review-changes
description: "Pre-commit code review. Use before committing to catch architecture violations, bugs, and security issues."
---

# Review Changes

Review all staged and unstaged changes before committing.

## 1. Architecture Check

- [ ] No business logic in API endpoints
- [ ] No DB queries outside infrastructure/
- [ ] Services don't import from API layer
- [ ] Domain models don't import from other layers
- [ ] Dependency injection used (no hard-coded dependencies)

## 2. Code Quality

- [ ] Type hints on all new/modified functions
- [ ] No magic strings — constants or enums used
- [ ] No `any` types in TypeScript
- [ ] Early returns instead of deep nesting
- [ ] No debugging code left (print, console.log, debugger)

## 3. Race Conditions

- [ ] All async operations awaited
- [ ] useEffect has cleanup function for async work
- [ ] AbortController used for fetch in effects
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

## Action

Report findings with file paths and line numbers. Suggest specific fixes for each issue.
