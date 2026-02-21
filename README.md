# claude-templates

A simple CLI to apply Claude Code project templates and best-practice modules to your projects.

## Install

```bash
# From local clone
uv tool install .

# From GitHub
uv tool install git+https://github.com/thomaspernet/claude-templates.git
```

## Usage

### Templates — Full project scaffolds

```bash
claude-templates list                          # List templates
claude-templates info coding                   # Show template details
claude-templates init coding                   # Apply to current directory
claude-templates init analysis ./my-project    # Apply to specific directory
claude-templates diff coding ./my-project      # Preview changes (dry run)
```

### Modules — Best-practice add-ons

```bash
claude-templates list-modules                  # List modules by category
claude-templates info-module agent-design      # Show module details
claude-templates add agent-design              # Add to current directory
claude-templates add fastapi ./my-project      # Add to specific directory
```

Modules can be layered — add as many as you need to any project:

```bash
claude-templates init coding ./my-api
claude-templates add fastapi ./my-api
claude-templates add pydantic ./my-api
claude-templates add security ./my-api
```

## Available Templates

| Template | Description |
|----------|-------------|
| `coding` | Full-stack development (Python + JS/TS, DDD architecture) |
| `analysis` | Data analysis (pandas, polars, notebooks, visualization) |
| `research` | Literature review, knowledge synthesis, academic writing |
| `data-engineering` | ETL pipelines, databases, data quality, orchestration |
| `writing` | Documentation, articles, style guides, editing workflows |

## Available Modules

### AI / LLM Engineering

| Module | Description |
|--------|-------------|
| `agent-design` | Agent architecture, tool design, instruction builders, anti-patterns |
| `prompt-engineering` | System prompt structure, instruction/rule/skill layers, testing prompts |

### Databases

| Module | Description |
|--------|-------------|
| `cypher-neo4j` | Cypher query patterns, MERGE vs CREATE, indexing, parameterized queries |
| `sql-postgres` | SQL style, CTEs, window functions, indexing, migrations, connection pooling |
| `data-modeling` | Schema design, normalization, graph modeling, naming conventions |

### Python Patterns

| Module | Description |
|--------|-------------|
| `fastapi` | Router organization, dependency injection, error handling, async endpoints |
| `pydantic` | Model patterns, validators, serialization, discriminated unions |
| `async-python` | asyncio patterns, event loop rules, common pitfalls, testing async code |

### Frontend

| Module | Description |
|--------|-------------|
| `react-nextjs` | Server/Client Components, App Router, state management, data fetching |
| `tailwind-css` | Utility conventions, responsive design, component extraction, dark mode |

### DevOps / Infrastructure

| Module | Description |
|--------|-------------|
| `docker` | Dockerfile best practices, multi-stage builds, compose, health checks |
| `ci-cd` | GitHub Actions patterns, test/lint/deploy stages, secrets handling |
| `git-workflow` | Branching strategy, PR conventions, conventional commits, code review |

### General Engineering

| Module | Description |
|--------|-------------|
| `testing-strategy` | Test pyramid, mocking strategy, fixture patterns, TDD workflow |
| `api-design` | REST conventions, versioning, pagination, error responses, OpenAPI |
| `logging-observability` | Structured logging, log levels, correlation IDs, tracing, metrics |
| `security` | OWASP top 10, input validation, auth patterns, secrets management |

## What Gets Installed

**Templates** apply a full project scaffold:

- `CLAUDE.md` — Project identity, architecture rules, dev commands
- `.claude/rules/` — Path-scoped rules for Claude Code
- `.claude/commands/` — Reusable command workflows
- `.claude/skills/` — Specialized skill definitions
- `.claude/settings.local.json` — Permission allowlist

**Modules** add focused best-practice files:

- `.claude/rules/<module>.md` — Best practices and anti-patterns
- `.claude/skills/<skill>/SKILL.md` — Workflow skills (some modules)

## Development

```bash
git clone https://github.com/thomaspernet/claude-templates.git
cd claude-templates
uv pip install -e ".[dev]"
.venv/bin/python -m pytest -v
```

## License

MIT
