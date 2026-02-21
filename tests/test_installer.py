"""Tests for the template installer logic."""

from pathlib import Path

from claude_templates.installer import (
    diff_template,
    ensure_gitignore_entries,
    install_template,
)


def _make_template(tmp_path: Path) -> Path:
    """Create a minimal template directory for testing."""
    tmpl = tmp_path / "template"
    tmpl.mkdir()
    (tmpl / "CLAUDE.md").write_text("# Test")
    sub = tmpl / ".claude" / "rules"
    sub.mkdir(parents=True)
    (sub / "test.md").write_text("rule content")
    return tmpl


def test_install_creates_files(tmp_path):
    tmpl = _make_template(tmp_path)
    target = tmp_path / "project"
    target.mkdir()

    created, skipped = install_template(tmpl, target)

    assert len(created) == 2
    assert len(skipped) == 0
    assert (target / "CLAUDE.md").exists()
    assert (target / ".claude" / "rules" / "test.md").exists()


def test_install_skips_existing_without_force(tmp_path):
    tmpl = _make_template(tmp_path)
    target = tmp_path / "project"
    target.mkdir()
    (target / "CLAUDE.md").write_text("existing")

    created, skipped = install_template(tmpl, target, force=False)

    assert Path("CLAUDE.md") in skipped
    assert (target / "CLAUDE.md").read_text() == "existing"


def test_install_overwrites_with_force(tmp_path):
    tmpl = _make_template(tmp_path)
    target = tmp_path / "project"
    target.mkdir()
    (target / "CLAUDE.md").write_text("existing")

    created, skipped = install_template(tmpl, target, force=True)

    assert len(skipped) == 0
    assert (target / "CLAUDE.md").read_text() == "# Test"


def test_diff_categorizes_files(tmp_path):
    tmpl = _make_template(tmp_path)
    target = tmp_path / "project"
    target.mkdir()
    (target / "CLAUDE.md").write_text("existing")

    new, existing = diff_template(tmpl, target)

    assert Path("CLAUDE.md") in existing
    assert Path(".claude/rules/test.md") in new


def test_ensure_gitignore_creates_file(tmp_path):
    ensure_gitignore_entries(tmp_path)

    gitignore = tmp_path / ".gitignore"
    assert gitignore.exists()
    content = gitignore.read_text()
    assert "CLAUDE.local.md" in content
    assert ".claude/settings.local.json" in content


def test_ensure_gitignore_appends_missing(tmp_path):
    gitignore = tmp_path / ".gitignore"
    gitignore.write_text("node_modules/\n")

    ensure_gitignore_entries(tmp_path)

    content = gitignore.read_text()
    assert "node_modules/" in content
    assert "CLAUDE.local.md" in content


def test_ensure_gitignore_skips_existing(tmp_path):
    gitignore = tmp_path / ".gitignore"
    gitignore.write_text("CLAUDE.local.md\n.claude/settings.local.json\n")

    ensure_gitignore_entries(tmp_path)

    content = gitignore.read_text()
    # Should not duplicate entries
    assert content.count("CLAUDE.local.md") == 1
