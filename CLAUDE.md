# claude-templates

A Python CLI tool for applying Claude Code project templates.

## Tech Stack

- Python 3.10+, Click for CLI
- Package manager: uv
- Templates stored as plain files in `src/claude_templates/_templates/`

## Project Structure

```
src/claude_templates/
  cli.py          — Click CLI entry point (list, info, init, diff)
  templates.py    — Template registry and path resolution
  installer.py    — File copy logic and conflict handling
  _templates/     — Template files shipped with the package
```

## Dev Commands

- `uv run claude-templates list` — test CLI
- `uv run pytest -v` — run tests
- `uv run ruff check src/ tests/` — lint

## Rules

- Templates are plain files (markdown, json). No Jinja rendering.
- Path resolution uses `importlib.resources.files()` for install compatibility.
- Every template must have at minimum: CLAUDE.md, .claude/settings.local.json, one rule file.
- Commit prefixes: `fix:`, `feat:`, `refactor:`, `docs:`, `chore:`, `test:`
