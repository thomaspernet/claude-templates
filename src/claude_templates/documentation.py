"""Documentation pack registry and path resolution."""

from importlib.resources import files
from pathlib import Path

DOCUMENTATION_DIR = files("claude_templates") / "_documentation"

DOCUMENTATION: dict[str, dict] = {
    "agents": {
        "category": "AI / LLM Engineering",
        "description": (
            "Agent design best practices, tool patterns, "
            "chatbot architecture, memory systems"
        ),
        "details": (
            "Pre-loaded general best practices for building LLM-based agents: "
            "writing AI instructions, agent design principles, chatbot and tool patterns, "
            "memory in agentic AI. Includes a project-specific scaffold for documenting "
            "your own agent architecture, tool catalog, and implementation patterns."
        ),
    },
    "econ-research-paper": {
        "category": "Academic / Research",
        "description": (
            "Economics research methodology, paper structure, "
            "identification strategy, tables and results presentation"
        ),
        "details": (
            "Pre-loaded general best practices for writing empirical economics papers: "
            "defining a research project (skeptic tests, contribution, feasibility), "
            "writing a paper (WHAT/WHY/HOW introduction, section-by-section guide, writing tips), "
            "identification and empirical strategy (IV, DiD, RD, RCT), "
            "tables, figures, and results presentation. "
            "Includes a project-specific scaffold for documenting your research design, "
            "data sources, empirical strategy, and revision log."
        ),
    },
}


def get_documentation_dir(name: str) -> Path:
    """Get the directory path for a documentation pack. Raises KeyError if not found."""
    if name not in DOCUMENTATION:
        raise KeyError(
            f"Unknown documentation pack: '{name}'. "
            "Use 'list-docs' to see available packs."
        )
    return Path(str(DOCUMENTATION_DIR / name))


def list_documentation_files(name: str) -> list[Path]:
    """List all files in a documentation pack, as relative paths."""
    doc_dir = get_documentation_dir(name)
    if not doc_dir.exists():
        return []
    return sorted(
        p.relative_to(doc_dir)
        for p in doc_dir.rglob("*")
        if p.is_file()
    )
