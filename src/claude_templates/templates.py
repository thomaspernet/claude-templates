"""Template registry and path resolution."""

from importlib.resources import files
from pathlib import Path


TEMPLATES_DIR = files("claude_templates") / "_templates"

TEMPLATES: dict[str, dict] = {
    "coding": {
        "description": "Full-stack development (Python + JS/TS, DDD architecture)",
        "details": (
            "Sets up a DDD architecture with strict layer separation, "
            "backend/frontend path-scoped rules, code review agent, "
            "and commit/verify workflows. Includes BUGS.md and MISTAKES.md tracking."
        ),
    },
    "analysis": {
        "description": "Data analysis (pandas, polars, notebooks, provenance tracking)",
        "details": (
            "Three-stage workflow: data-source (raw downloads), data-processing "
            "(clean, enrich), data-analysis (figures, tables). Provenance tracking, "
            "process-over-code explanations, EDA skills, and paper section drafting."
        ),
    },
    "research": {
        "description": "Literature review, knowledge synthesis, academic writing",
        "details": (
            "Sets up source evaluation rules, citation management, academic writing "
            "conventions, literature search commands, and source synthesis skills. "
            "Includes WebFetch permissions for scholarly sources."
        ),
    },
    "data-engineering": {
        "description": "ETL pipelines, databases, data quality, orchestration",
        "details": (
            "Configures pipeline idempotency rules, database conventions, "
            "validation workflows, and pipeline building skills. "
            "Includes BUGS.md and MISTAKES.md tracking."
        ),
    },
    "writing": {
        "description": "Documentation, articles, style guides, editing workflows",
        "details": (
            "Sets up style guide rules, review process workflows, "
            "draft review commands, and document writing skills."
        ),
    },
    "research-analytics": {
        "description": "Academic research with data pipelines (AWS Athena, paper tables/figures)",
        "details": (
            "Three-stage workflow: data-source (external downloads to S3/Glue), "
            "data-processing (Athena queries, enrichment), data-analysis (paper figures/tables). "
            "Agent explains process not code, traces provenance, and drafts paper sections."
        ),
    },
}


def get_template_dir(name: str) -> Path:
    """Get the directory path for a template. Raises KeyError if not found."""
    if name not in TEMPLATES:
        raise KeyError(f"Unknown template: '{name}'. Use 'list' to see available templates.")
    return Path(str(TEMPLATES_DIR / name))


def list_template_files(name: str) -> list[Path]:
    """List all files in a template, as relative paths."""
    template_dir = get_template_dir(name)
    if not template_dir.exists():
        return []
    return sorted(
        p.relative_to(template_dir)
        for p in template_dir.rglob("*")
        if p.is_file()
    )
