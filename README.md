# claude-templates

A simple CLI to apply Claude Code project templates to your projects.

## Install

```bash
# From local clone
uv tool install .

# From GitHub
uv tool install git+https://github.com/thomaspernet/claude-templates.git
```

## Usage

```bash
# List available templates
claude-templates list

# Show template details
claude-templates info coding

# Apply a template to current directory
claude-templates init coding

# Apply to a specific directory
claude-templates init analysis ./my-analysis-project

# Preview what would change (dry run)
claude-templates diff coding ./my-project
```

## Available Templates

| Template | Description |
|----------|-------------|
| `coding` | Full-stack development (Python + JS/TS, DDD architecture) |
| `analysis` | Data analysis (pandas, polars, notebooks, visualization) |
| `research` | Literature review, knowledge synthesis, academic writing |
| `data-engineering` | ETL pipelines, databases, data quality, orchestration |
| `writing` | Documentation, articles, style guides, editing workflows |

## What Gets Installed

Each template applies a set of Claude Code configuration files to your project:

- `CLAUDE.md` — Project identity, architecture rules, dev commands
- `.claude/rules/` — Path-scoped rules for Claude Code
- `.claude/commands/` — Reusable command workflows
- `.claude/skills/` — Specialized skill definitions
- `.claude/settings.local.json` — Permission allowlist

Some templates also include `BUGS.md`, `MISTAKES.md`, and `CLAUDE.local.md.example`.

## Development

```bash
git clone https://github.com/thomaspernet/claude-templates.git
cd claude-templates
uv sync --dev
uv run pytest -v
```

## License

MIT
