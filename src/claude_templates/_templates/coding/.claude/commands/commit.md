# Commit Workflow

Safe commit process with pre-flight checks.

## Steps

1. **Check tracking files** — Have BUGS.md or MISTAKES.md been updated this session? If yes, include them.
2. **Review diff** — Run `git diff --staged`. Check for:
   - Architecture violations (DB queries outside infrastructure/, logic in API)
   - Hardcoded secrets or credentials
   - Missing type hints on new functions
   - Debugging code left in (print statements, console.log)
3. **Stage files** — Stage specific files (never `git add -A` for sensitive repos).
4. **Commit** — Use conventional prefix: `fix:`, `feat:`, `refactor:`, `docs:`, `chore:`, `test:`
5. **Push** — Push to remote. NEVER force push without explicit permission.

## Commit Message Format

```
<prefix>: <concise description>

<optional body explaining why, not what>
```
