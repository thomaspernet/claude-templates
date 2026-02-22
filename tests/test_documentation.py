"""Tests that validate all documentation packs have required files."""

import pytest

from claude_templates.documentation import (
    DOCUMENTATION,
    get_documentation_dir,
    list_documentation_files,
)

DOC_NAMES = list(DOCUMENTATION.keys())


@pytest.mark.parametrize("name", DOC_NAMES)
def test_documentation_directory_exists(name):
    doc_dir = get_documentation_dir(name)
    assert doc_dir.exists(), f"Documentation directory missing: {doc_dir}"


@pytest.mark.parametrize("name", DOC_NAMES)
def test_documentation_has_rule_file(name):
    files = [str(f) for f in list_documentation_files(name)]
    rules = [f for f in files if ".claude/rules/" in f]
    assert len(rules) >= 1, f"Documentation pack '{name}' has no rule files"


@pytest.mark.parametrize("name", DOC_NAMES)
def test_documentation_has_general_best_practices(name):
    """Each documentation pack must include general best practices."""
    files = [str(f) for f in list_documentation_files(name)]
    best_practices = [f for f in files if "general-best-practices/" in f]
    assert len(best_practices) >= 1, f"Documentation pack '{name}' has no best practice files"


@pytest.mark.parametrize("name", DOC_NAMES)
def test_documentation_has_project_specific_scaffold(name):
    """Each documentation pack must include a project-specific scaffold."""
    files = [str(f) for f in list_documentation_files(name)]
    project_specific = [f for f in files if "project-specific/" in f]
    assert len(project_specific) >= 1, (
        f"Documentation pack '{name}' has no project-specific scaffold"
    )


def test_get_documentation_dir_unknown():
    with pytest.raises(KeyError, match="Unknown documentation pack"):
        get_documentation_dir("nonexistent")


def test_all_documentation_have_category():
    for name, meta in DOCUMENTATION.items():
        assert "category" in meta, f"Documentation pack '{name}' missing category"


def test_all_documentation_have_description():
    for name, meta in DOCUMENTATION.items():
        assert "description" in meta, f"Documentation pack '{name}' missing description"
        assert len(meta["description"]) > 10, f"Documentation pack '{name}' description too short"


def test_all_documentation_have_details():
    for name, meta in DOCUMENTATION.items():
        assert "details" in meta, f"Documentation pack '{name}' missing details"
        assert len(meta["details"]) > 20, f"Documentation pack '{name}' details too short"
