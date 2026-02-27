---
name: write-tests
description: "Use this skill when adding tests to new or existing code. Invoke when the user mentions writing tests, improving coverage, setting up a test suite, or asks how to test a function or feature — even if they haven't decided which test types are needed."
---

# Write Tests

## When to Use

**Perfect for:**
- Adding tests to a new feature before or after implementation
- Filling a coverage gap in existing functionality
- Setting up the test infrastructure for a new module

**Not ideal for:**
- Snapshot or visual regression tests (use a dedicated visual testing tool)
- Load and performance testing (use k6, Locust, or similar)
- Tests for code you haven't read — understand the implementation first

---

> **Core Philosophy:** Tests are specifications, not proof of correctness. A test that only checks the happy path gives false confidence. Write tests that would catch real bugs: wrong logic, missing validation, broken error propagation, and state leakage between tests.

## ⚠️ CRITICAL

1. **Each test must be fully independent.** A test that only passes when run after another test is not a test — it's a timing dependency. Use fixtures, rollbacks, or fresh instances to guarantee isolation.
2. **Test behavior, not implementation.** Call public interfaces, not private methods. If a refactor breaks your tests without changing behavior, the tests are wrong.
3. **Read the code before writing tests.** You must understand what the function actually does — including edge cases and error paths — before you can write meaningful tests. Never write tests from function signatures alone.

---

## Step 1: Identify What to Test

Before writing a single test:
- Read the implementation of every function you'll test
- List all public functions/methods and their contracts
- Map inputs → expected outputs for each
- List edge cases: empty, null, boundary values, large input
- List error cases: invalid input, missing dependencies, failed external calls
- Identify external dependencies that need mocking (DB, APIs, filesystem)

## Step 2: Write Unit Tests

For each function, write tests in this order:
1. **Happy path** — normal expected input → correct output
2. **Edge cases** — empty, boundary, minimum/maximum values
3. **Error cases** — invalid input, exceptions raised correctly
4. **Mocked dependencies** — verify correct calls to external interfaces

Naming convention: `test_{function}_{scenario}_{expected_result}`

Examples:
```
test_create_user_valid_input_returns_user_id
test_create_user_duplicate_email_raises_value_error
test_create_user_missing_name_raises_validation_error
```

## Step 3: Write Integration Tests

For interactions between components:
1. **API endpoints** — test via test client with full request/response cycle
2. **Service + repository** — test together with a test database or in-memory store
3. **Error propagation** — verify a DB error surfaces correctly as a 500, a validation error as a 400

Integration tests are slower — keep them focused on cross-layer contracts, not logic already covered by unit tests.

## Step 4: Add Fixtures

Create reusable fixtures for:
- Sample data objects (valid and invalid)
- Database sessions with automatic rollback
- Mocked external services (use `pytest-mock` or `unittest.mock`)
- Temporary files/directories (`tmp_path` in pytest)

Keep fixtures in `conftest.py` at the appropriate scope. Don't recreate setup logic in individual tests.

## Step 5: Verify

Before marking tests complete:
- Run full test suite — all pass
- Run new tests in isolation — still pass (no hidden ordering dependency)
- Check coverage on new code: aim for 80%+ on business logic
- Verify unit suite runs in under 10 seconds
- Remove any `print` or debugging statements left in tests

## Output

Report a summary of what was written:

```
## Tests: {Feature Name}

Unit tests ({n}):
  tests/unit/test_{module}.py
  - test_{fn}_happy_path
  - test_{fn}_empty_input
  - test_{fn}_invalid_type_raises_error

Integration tests ({n}):
  tests/integration/test_{module}.py
  - test_{endpoint}_returns_200_on_valid_request
  - test_{endpoint}_returns_400_on_missing_field

Fixtures added:
  tests/conftest.py
  - {fixture_name}: {purpose}

Coverage on new code: {n}%
All tests pass independently: ✓
```

## Checklist

- [ ] Implementation read before tests written
- [ ] Happy path tested for each public function
- [ ] Edge cases covered (empty, null, boundary)
- [ ] Error cases tested (invalid input, exceptions propagate correctly)
- [ ] External dependencies mocked — tests don't hit real DBs/APIs
- [ ] Fixtures created for reusable setup
- [ ] Each test passes independently (no ordering dependency)
- [ ] Coverage on new code at 80%+
- [ ] No debugging code left in tests
- [ ] Full test suite passes
