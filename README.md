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

### Documentation — Best-practice reference packs

```bash
claude-templates list-docs                    # List documentation packs
claude-templates info-doc agents              # Show pack details
claude-templates add-doc agents               # Add to current directory
claude-templates add-doc agents ./my-project  # Add to specific directory
```

Documentation packs install general best practices and a project-specific scaffold into `documentation/`. The coding agent uses these as benchmarks when implementing features.

## Available Templates

| Template | Description | Details |
|----------|-------------|---------|
| `coding` | Full-stack development (Python + JS/TS, DDD architecture) | DDD 4-layer architecture, backend/frontend path-scoped rules, code review agent, commit/verify workflows, BUGS.md and MISTAKES.md tracking |
| `analysis` | Data analysis (pandas, polars, notebooks, provenance tracking) | Three-stage workflow (data-source → data-processing → data-analysis), provenance tracking, process-over-code explanations, EDA skills, paper section drafting |
| `research` | Literature review, knowledge synthesis, academic writing | Source evaluation rules, citation management, academic writing conventions, literature search commands, WebFetch permissions |
| `data-engineering` | ETL pipelines, databases, data quality, orchestration | Pipeline idempotency rules, database conventions, validation workflows, pipeline building skills, BUGS.md and MISTAKES.md tracking |
| `writing` | Documentation, articles, style guides, editing workflows | Style guide rules, review process workflows, draft review commands, document writing skills |
| `research-analytics` | Academic research with data pipelines (AWS Athena, paper tables/figures) | Three-stage workflow (data-source → data-processing → data-analysis), provenance tracking, paper section drafting, explain-table command |

## Available Modules

| Module | Category | Description |
|--------|----------|-------------|
| `agent-design` | AI / LLM Engineering | Agent architecture, tool design, instruction builders, anti-patterns |
| `prompt-engineering` | AI / LLM Engineering | System prompt structure, instruction/rule/skill layers, testing prompts |
| `cypher-neo4j` | Databases | Cypher query patterns, MERGE vs CREATE, indexing, parameterized queries |
| `sql-postgres` | Databases | SQL style, CTEs, window functions, indexing, migrations, connection pooling |
| `data-modeling` | Databases | Schema design, normalization, graph modeling, naming conventions |
| `fastapi` | Python Patterns | Router organization, dependency injection, error handling, async endpoints |
| `pydantic` | Python Patterns | Model patterns, validators, serialization, discriminated unions |
| `async-python` | Python Patterns | asyncio patterns, event loop rules, common pitfalls, testing async code |
| `notebook` | Python Patterns | Notebook style, markdown cells, code extraction, autoreload, exportable documents |
| `react-nextjs` | Frontend | Server/Client Components, App Router, state management, data fetching |
| `tailwind-css` | Frontend | Utility conventions, responsive design, component extraction, dark mode |
| `docker` | DevOps / Infrastructure | Dockerfile best practices, multi-stage builds, compose, health checks |
| `ci-cd` | DevOps / Infrastructure | GitHub Actions patterns, test/lint/deploy stages, secrets handling |
| `git-workflow` | DevOps / Infrastructure | Branching strategy, PR conventions, conventional commits, code review |
| `econ-research-paper` | Academic / Research | Economics paper structure, WHAT/WHY/HOW introduction, identification strategy, robustness checks |
| `econ-peer-review` | Academic / Research | Peer review structure, evaluation checklists, econometric design assessment, tone and ethics |
| `testing-strategy` | General Engineering | Test pyramid, mocking strategy, fixture patterns, TDD workflow |
| `api-design` | General Engineering | REST conventions, versioning, pagination, error responses, OpenAPI |
| `logging-observability` | General Engineering | Structured logging, log levels, correlation IDs, tracing, metrics |
| `security` | General Engineering | OWASP top 10, input validation, auth patterns, secrets management |

## Available Documentation Packs

| Pack       | Category             | Description                                                                      |
|------------|----------------------|----------------------------------------------------------------------------------|
| `agents`   | AI / LLM Engineering | Agent design best practices, tool patterns, chatbot architecture, memory systems |
| `econ-research-paper` | Academic / Research | Economics research methodology, paper structure, identification strategy, tables and results |
| `econ-peer-review` | Academic / Research | Peer review methodology, econometric design evaluation, tone and ethics, evaluation checklists |

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

**Documentation packs** add reference docs and project scaffolds:

- `documentation/<topic>/general-best-practices/` — Pre-loaded industry best practices
- `documentation/<topic>/project-specific/` — Scaffold for documenting your project's implementation
- `.claude/rules/documentation-<topic>.md` — Rule telling the coding agent how to use and maintain the docs

## Development

```bash
git clone https://github.com/thomaspernet/claude-templates.git
cd claude-templates
uv pip install -e ".[dev]"
.venv/bin/python -m pytest -v
```

## License

MIT
