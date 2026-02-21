# Verify Project

Run all checks to ensure the project is in a healthy state.

## Steps

1. **Git status** — Check for uncommitted changes
2. **Backend tests** — Run `uv run pytest -v`. ALL tests must pass.
3. **Backend lint** — Run `uv run ruff check`. Zero errors.
4. **Frontend build** — Run `npm run build`. Must complete without errors.
5. **Frontend lint** — Run `npm run lint`. Zero errors.

## Report

Print a summary table:

| Check | Status |
|-------|--------|
| Backend tests | PASS / FAIL (N passed, M failed) |
| Backend lint | PASS / FAIL (N issues) |
| Frontend build | PASS / FAIL |
| Frontend lint | PASS / FAIL (N issues) |

If ANY check fails, list the specific errors and suggest fixes.
