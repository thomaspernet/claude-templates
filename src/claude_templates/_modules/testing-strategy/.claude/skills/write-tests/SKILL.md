---
name: write-tests
description: "Guided test creation for a feature. Use when adding tests to new or existing functionality."
---

# Write Tests

Follow these steps to create comprehensive tests for a feature.

## Step 1: Identify What to Test

- What are the public functions/methods?
- What are the inputs and expected outputs?
- What are the edge cases? (empty, null, max, error)
- What external dependencies need mocking?

## Step 2: Write Unit Tests

For each function:
1. Test the happy path (normal expected input)
2. Test edge cases (empty, boundary values)
3. Test error cases (invalid input, missing data)
4. Test with mock dependencies if needed

Naming: `test_{function}_{scenario}_{expected}`

## Step 3: Write Integration Tests

For interactions between components:
1. Test API endpoints with test client
2. Test service + repository together (with test DB if applicable)
3. Test error propagation across layers

## Step 4: Add Fixtures

Create reusable test fixtures for:
- Sample data objects
- Database sessions (with rollback)
- Mocked external services
- Temporary files/directories

## Step 5: Verify

- Run full test suite: all pass
- Check coverage on new code: aim for 80%+
- Verify no test depends on another test's state
- Verify tests run fast (unit suite < 10 seconds)

## Checklist

- [ ] Happy path tested for each function
- [ ] Edge cases covered (empty, null, boundary)
- [ ] Error cases tested (invalid input, exceptions)
- [ ] External dependencies mocked
- [ ] Fixtures created for reusable setup
- [ ] All tests pass independently
- [ ] Coverage meets target (80%+)
