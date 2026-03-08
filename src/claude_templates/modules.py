"""Module registry and path resolution."""

from importlib.resources import files
from pathlib import Path


MODULES_DIR = files("claude_templates") / "_modules"

MODULES: dict[str, dict] = {
    # AI / LLM Engineering
    "agent-design": {
        "category": "AI / LLM Engineering",
        "description": "Agent architecture, tool design, instruction builders, anti-patterns",
        "has_skill": True,
    },
    "prompt-engineering": {
        "category": "AI / LLM Engineering",
        "description": "System prompt structure, instruction/rule/skill layers, testing prompts",
        "has_skill": True,
    },
    # Databases
    "cypher-neo4j": {
        "category": "Databases",
        "description": "Cypher query patterns, MERGE vs CREATE, indexing, parameterized queries",
        "has_skill": False,
    },
    "ladybugdb": {
        "category": "Databases",
        "description": (
            "LadybugDB embedded graph: schema design, Cypher patterns, "
            "bulk loading, DuckDB interop, graph algorithms"
        ),
        "has_skill": False,
    },
    "sql-postgres": {
        "category": "Databases",
        "description": "SQL style, CTEs, window functions, indexing, migrations, connection pooling",
        "has_skill": False,
    },
    "data-modeling": {
        "category": "Databases",
        "description": "Schema design, normalization, graph modeling, naming conventions",
        "has_skill": False,
    },
    # Python Patterns
    "fastapi": {
        "category": "Python Patterns",
        "description": "Router organization, dependency injection, error handling, async endpoints",
        "has_skill": False,
    },
    "pydantic": {
        "category": "Python Patterns",
        "description": "Model patterns, validators, serialization, discriminated unions",
        "has_skill": False,
    },
    "async-python": {
        "category": "Python Patterns",
        "description": "asyncio patterns, event loop rules, common pitfalls, testing async code",
        "has_skill": False,
    },
    "notebook": {
        "category": "Python Patterns",
        "description": "Notebook style, markdown cells, code extraction, autoreload, exportable documents",
        "has_skill": False,
    },
    # Frontend
    "react-nextjs": {
        "category": "Frontend",
        "description": "Server/Client Components, App Router, state management, data fetching",
        "has_skill": False,
    },
    "tailwind-css": {
        "category": "Frontend",
        "description": "Utility conventions, responsive design, component extraction, dark mode",
        "has_skill": False,
    },
    # DevOps / Infrastructure
    "docker": {
        "category": "DevOps / Infrastructure",
        "description": "Dockerfile best practices, multi-stage builds, compose, health checks",
        "has_skill": False,
    },
    "ci-cd": {
        "category": "DevOps / Infrastructure",
        "description": "GitHub Actions patterns, test/lint/deploy stages, secrets handling",
        "has_skill": False,
    },
    "git-workflow": {
        "category": "DevOps / Infrastructure",
        "description": "Branching strategy, PR conventions, conventional commits, code review",
        "has_skill": False,
    },
    # Academic / Research
    "econ-research-paper": {
        "category": "Academic / Research",
        "description": (
            "Economics paper structure, WHAT/WHY/HOW introduction, "
            "identification strategy, robustness checks"
        ),
        "has_skill": True,
    },
    "econ-peer-review": {
        "category": "Academic / Research",
        "description": (
            "Peer review structure, evaluation checklists, "
            "econometric design assessment, tone and ethics"
        ),
        "has_skill": True,
    },
    # General Engineering
    "testing-strategy": {
        "category": "General Engineering",
        "description": "Test pyramid, mocking strategy, fixture patterns, TDD workflow",
        "has_skill": True,
    },
    "api-design": {
        "category": "General Engineering",
        "description": "REST conventions, versioning, pagination, error responses, OpenAPI",
        "has_skill": False,
    },
    "logging-observability": {
        "category": "General Engineering",
        "description": "Structured logging, log levels, correlation IDs, tracing, metrics",
        "has_skill": False,
    },
    "security": {
        "category": "General Engineering",
        "description": "OWASP top 10, input validation, auth patterns, secrets management",
        "has_skill": False,
    },
}


def get_module_dir(name: str) -> Path:
    """Get the directory path for a module. Raises KeyError if not found."""
    if name not in MODULES:
        raise KeyError(f"Unknown module: '{name}'. Use 'list-modules' to see available modules.")
    return Path(str(MODULES_DIR / name))


def list_module_files(name: str) -> list[Path]:
    """List all files in a module, as relative paths."""
    module_dir = get_module_dir(name)
    if not module_dir.exists():
        return []
    return sorted(
        p.relative_to(module_dir)
        for p in module_dir.rglob("*")
        if p.is_file()
    )
