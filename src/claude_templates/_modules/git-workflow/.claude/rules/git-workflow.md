# Git Workflow Best Practices

## Branching Strategy

### Trunk-Based (Recommended for small teams)

- `main` is always deployable
- Short-lived feature branches (1-3 days max)
- Merge via PR with review
- Delete branches after merge

### Branch Naming

```
feat/add-user-auth
fix/login-redirect-loop
refactor/extract-payment-service
docs/api-reference
chore/upgrade-dependencies
```

Format: `{type}/{short-description}` using kebab-case.

## Commit Messages

### Conventional Commits

```
<type>: <description>

[optional body explaining why, not what]
```

Types:
- `feat:` — new feature
- `fix:` — bug fix
- `refactor:` — code change that neither fixes nor adds
- `docs:` — documentation only
- `test:` — adding or fixing tests
- `chore:` — maintenance (deps, config, CI)

### Rules

- Subject line under 72 characters
- Imperative mood: "Add feature" not "Added feature"
- Body explains **why**, not what (the diff shows what)
- Reference issue numbers: `fix: resolve login loop (#42)`

## Pull Requests

### Size

- Keep PRs small: under 400 lines changed
- One logical change per PR
- If a PR touches more than 10 files, consider splitting

### PR Description

```markdown
## What
Brief description of the change.

## Why
Context and motivation.

## Testing
How you verified the change works.
```

### Review Checklist

- [ ] Code compiles and tests pass
- [ ] No unrelated changes included
- [ ] Error handling is appropriate
- [ ] No hardcoded secrets or credentials
- [ ] New code has tests
- [ ] Documentation updated if needed

## Merging

- **Squash merge** for feature branches (clean history)
- **Merge commit** for release branches (preserve history)
- **Rebase** for keeping up with main (before PR, not after review)
- NEVER force push to shared branches (main, develop)

## Release Tagging

```bash
git tag -a v1.2.0 -m "Release 1.2.0: add user auth, fix payment bug"
git push origin v1.2.0
```

- Use semantic versioning: `v{major}.{minor}.{patch}`
- Major: breaking changes
- Minor: new features, backward compatible
- Patch: bug fixes

## Anti-Patterns — NEVER Do

1. **Long-lived feature branches** — merge frequently, at most every few days
2. **Force push to main** — destroys shared history
3. **Giant PRs** — impossible to review properly
4. **Vague commit messages** — "fix stuff", "update", "wip"
5. **Committing secrets** — use .gitignore and pre-commit hooks
6. **No PR reviews** — even solo devs benefit from self-review via PR
