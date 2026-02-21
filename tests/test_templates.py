"""Tests that validate all templates have required files."""

import pytest

from claude_templates.templates import TEMPLATES, get_template_dir, list_template_files


TEMPLATE_NAMES = list(TEMPLATES.keys())


@pytest.mark.parametrize("name", TEMPLATE_NAMES)
def test_template_directory_exists(name):
    template_dir = get_template_dir(name)
    assert template_dir.exists(), f"Template directory missing: {template_dir}"


@pytest.mark.parametrize("name", TEMPLATE_NAMES)
def test_template_has_claude_md(name):
    files = [str(f) for f in list_template_files(name)]
    assert "CLAUDE.md" in files, f"Template '{name}' missing CLAUDE.md"


@pytest.mark.parametrize("name", TEMPLATE_NAMES)
def test_template_has_settings(name):
    files = [str(f) for f in list_template_files(name)]
    assert ".claude/settings.local.json" in files, (
        f"Template '{name}' missing .claude/settings.local.json"
    )


@pytest.mark.parametrize("name", TEMPLATE_NAMES)
def test_template_has_at_least_one_rule(name):
    files = [str(f) for f in list_template_files(name)]
    rules = [f for f in files if ".claude/rules/" in f]
    assert len(rules) >= 1, f"Template '{name}' has no rules"


@pytest.mark.parametrize("name", TEMPLATE_NAMES)
def test_template_has_at_least_one_skill_or_command(name):
    files = [str(f) for f in list_template_files(name)]
    skills = [f for f in files if ".claude/skills/" in f]
    commands = [f for f in files if ".claude/commands/" in f]
    assert len(skills) + len(commands) >= 1, (
        f"Template '{name}' has no skills or commands"
    )


def test_get_template_dir_unknown():
    with pytest.raises(KeyError, match="Unknown template"):
        get_template_dir("nonexistent")


def test_all_templates_have_description():
    for name, meta in TEMPLATES.items():
        assert "description" in meta, f"Template '{name}' missing description"
        assert len(meta["description"]) > 10, f"Template '{name}' description too short"
