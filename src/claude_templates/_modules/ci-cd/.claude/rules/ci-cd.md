# CI/CD Best Practices (GitHub Actions)

## Workflow Structure

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install ruff && ruff check .

  test:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -e ".[dev]" && pytest

  deploy:
    runs-on: ubuntu-latest
    needs: test
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - run: echo "Deploy here"
```

## Pipeline Stages

| Stage | Purpose | Fail = Block? |
|-------|---------|---------------|
| Lint | Code style, formatting | Yes |
| Test | Unit + integration tests | Yes |
| Build | Compile, bundle, Docker image | Yes |
| Deploy (staging) | Deploy to staging env | Yes (for prod) |
| Deploy (prod) | Deploy to production | N/A |

Run lint first — it's fastest and catches issues cheaply.

## Caching

Cache dependencies to speed up builds:

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements*.txt') }}
    restore-keys: ${{ runner.os }}-pip-
```

For Node.js:
```yaml
- uses: actions/cache@v4
  with:
    path: node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
```

## Matrix Builds

Test across multiple versions:

```yaml
strategy:
  matrix:
    python-version: ["3.10", "3.11", "3.12"]
    os: [ubuntu-latest, macos-latest]
```

## Secrets Handling

- Store secrets in GitHub Settings > Secrets and variables
- Reference with `${{ secrets.API_KEY }}`
- NEVER echo secrets in logs
- NEVER hardcode secrets in workflow files
- Use environment-specific secrets for staging/prod

## Branch Protection

- Require PR reviews before merge
- Require status checks (lint, test) to pass
- Require branches to be up to date with main
- Protect main branch from force pushes
- Require signed commits (optional, stricter)

## Release Automation

```yaml
on:
  push:
    tags: ["v*"]

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: gh release create ${{ github.ref_name }} --generate-notes
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Anti-Patterns — NEVER Do

1. **Secrets in workflow files** — use GitHub Secrets
2. **No caching** — rebuilds take 5x longer than needed
3. **Deploy without tests passing** — use `needs:` to enforce order
4. **Single monolithic job** — split into lint/test/build/deploy for parallelism
5. **No branch protection** — anyone can push broken code to main
6. **Manual deployments** — automate everything that can be automated
