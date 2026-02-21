"""Tests that validate all modules have required files."""

import pytest

from claude_templates.modules import MODULES, get_module_dir, list_module_files


MODULE_NAMES = list(MODULES.keys())


@pytest.mark.parametrize("name", MODULE_NAMES)
def test_module_directory_exists(name):
    module_dir = get_module_dir(name)
    assert module_dir.exists(), f"Module directory missing: {module_dir}"


@pytest.mark.parametrize("name", MODULE_NAMES)
def test_module_has_rule_file(name):
    files = [str(f) for f in list_module_files(name)]
    rules = [f for f in files if ".claude/rules/" in f]
    assert len(rules) >= 1, f"Module '{name}' has no rule files"


@pytest.mark.parametrize("name", MODULE_NAMES)
def test_module_rule_file_matches_name(name):
    """Rule file should be named after the module."""
    files = [str(f) for f in list_module_files(name)]
    expected = f".claude/rules/{name}.md"
    assert expected in files, f"Module '{name}' missing expected rule file: {expected}"


def test_modules_with_skills_have_skill_files():
    """Modules declared with has_skill=True must have skill files."""
    for name, meta in MODULES.items():
        if meta.get("has_skill"):
            files = [str(f) for f in list_module_files(name)]
            skills = [f for f in files if ".claude/skills/" in f]
            assert len(skills) >= 1, f"Module '{name}' declared has_skill=True but has no skills"


def test_get_module_dir_unknown():
    with pytest.raises(KeyError, match="Unknown module"):
        get_module_dir("nonexistent")


def test_all_modules_have_category():
    for name, meta in MODULES.items():
        assert "category" in meta, f"Module '{name}' missing category"


def test_all_modules_have_description():
    for name, meta in MODULES.items():
        assert "description" in meta, f"Module '{name}' missing description"
        assert len(meta["description"]) > 10, f"Module '{name}' description too short"
