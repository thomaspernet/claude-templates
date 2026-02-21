"""Tests for the module CLI commands."""

from click.testing import CliRunner

from claude_templates.cli import main


runner = CliRunner()


def test_list_modules_shows_categories():
    result = runner.invoke(main, ["list-modules"])
    assert result.exit_code == 0
    assert "AI / LLM Engineering" in result.output
    assert "Databases" in result.output
    assert "Python Patterns" in result.output
    assert "Frontend" in result.output
    assert "DevOps / Infrastructure" in result.output
    assert "General Engineering" in result.output


def test_list_modules_shows_all_modules():
    result = runner.invoke(main, ["list-modules"])
    assert result.exit_code == 0
    assert "agent-design" in result.output
    assert "cypher-neo4j" in result.output
    assert "fastapi" in result.output
    assert "react-nextjs" in result.output
    assert "docker" in result.output
    assert "security" in result.output


def test_info_module_known():
    result = runner.invoke(main, ["info-module", "agent-design"])
    assert result.exit_code == 0
    assert "agent-design" in result.output
    assert "AI / LLM Engineering" in result.output
    assert "Files:" in result.output


def test_info_module_unknown():
    result = runner.invoke(main, ["info-module", "nonexistent"])
    assert result.exit_code != 0
    assert "Unknown module" in result.output


def test_add_creates_files(tmp_path):
    result = runner.invoke(main, ["add", "agent-design", str(tmp_path)])
    assert result.exit_code == 0
    assert "Added" in result.output
    assert (tmp_path / ".claude" / "rules" / "agent-design.md").exists()
    assert (tmp_path / ".claude" / "skills" / "design-agent" / "SKILL.md").exists()


def test_add_rule_only_module(tmp_path):
    result = runner.invoke(main, ["add", "sql-postgres", str(tmp_path)])
    assert result.exit_code == 0
    assert (tmp_path / ".claude" / "rules" / "sql-postgres.md").exists()


def test_add_unknown_module(tmp_path):
    result = runner.invoke(main, ["add", "nonexistent", str(tmp_path)])
    assert result.exit_code != 0
    assert "Unknown module" in result.output


def test_add_skips_existing_files(tmp_path):
    # First add
    runner.invoke(main, ["add", "security", str(tmp_path)])
    rule_file = tmp_path / ".claude" / "rules" / "security.md"
    rule_file.write_text("custom")

    # Second add without --force — answer 'n'
    result = runner.invoke(main, ["add", "security", str(tmp_path)], input="n\n")
    assert "already exist" in result.output
    assert rule_file.read_text() == "custom"


def test_add_force_overwrites(tmp_path):
    runner.invoke(main, ["add", "security", str(tmp_path)])
    rule_file = tmp_path / ".claude" / "rules" / "security.md"
    rule_file.write_text("custom")

    result = runner.invoke(main, ["add", "security", str(tmp_path), "--force"])
    assert result.exit_code == 0
    assert rule_file.read_text() != "custom"


def test_add_multiple_modules_to_same_project(tmp_path):
    """Modules can be layered onto the same project."""
    runner.invoke(main, ["add", "fastapi", str(tmp_path)])
    runner.invoke(main, ["add", "pydantic", str(tmp_path)])
    runner.invoke(main, ["add", "async-python", str(tmp_path)])

    assert (tmp_path / ".claude" / "rules" / "fastapi.md").exists()
    assert (tmp_path / ".claude" / "rules" / "pydantic.md").exists()
    assert (tmp_path / ".claude" / "rules" / "async-python.md").exists()
