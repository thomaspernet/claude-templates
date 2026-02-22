"""Tests for the documentation CLI commands."""

from click.testing import CliRunner

from claude_templates.cli import main

runner = CliRunner()


def test_list_docs_shows_categories():
    result = runner.invoke(main, ["list-docs"])
    assert result.exit_code == 0
    assert "AI / LLM Engineering" in result.output


def test_list_docs_shows_all_packs():
    result = runner.invoke(main, ["list-docs"])
    assert result.exit_code == 0
    assert "agents" in result.output


def test_info_doc_known():
    result = runner.invoke(main, ["info-doc", "agents"])
    assert result.exit_code == 0
    assert "agents" in result.output
    assert "AI / LLM Engineering" in result.output
    assert "Files:" in result.output


def test_info_doc_unknown():
    result = runner.invoke(main, ["info-doc", "nonexistent"])
    assert result.exit_code != 0
    assert "Unknown documentation pack" in result.output


def test_add_doc_creates_files(tmp_path):
    result = runner.invoke(main, ["add-doc", "agents", str(tmp_path)])
    assert result.exit_code == 0
    assert "Added" in result.output
    rules = tmp_path / ".claude" / "rules" / "documentation-agents.md"
    assert rules.exists()
    bp = tmp_path / "documentation" / "agents" / "general-best-practices"
    assert (bp / "01-writing-ai-instructions.md").exists()
    assert (bp / "02-agent-design-principles.md").exists()
    assert (bp / "03-chatbot-and-tool-patterns.md").exists()
    assert (bp / "04-memory-in-agentic-ai.md").exists()
    ps = tmp_path / "documentation" / "agents" / "project-specific"
    assert (ps / "README.md").exists()
    assert (ps / "01-overview.md").exists()


def test_add_doc_unknown(tmp_path):
    result = runner.invoke(main, ["add-doc", "nonexistent", str(tmp_path)])
    assert result.exit_code != 0
    assert "Unknown documentation pack" in result.output


def test_add_doc_skips_existing_files(tmp_path):
    # First add
    runner.invoke(main, ["add-doc", "agents", str(tmp_path)])
    rule_file = tmp_path / ".claude" / "rules" / "documentation-agents.md"
    rule_file.write_text("custom")

    # Second add without --force — answer 'n'
    result = runner.invoke(main, ["add-doc", "agents", str(tmp_path)], input="n\n")
    assert "already exist" in result.output
    assert rule_file.read_text() == "custom"


def test_add_doc_force_overwrites(tmp_path):
    runner.invoke(main, ["add-doc", "agents", str(tmp_path)])
    rule_file = tmp_path / ".claude" / "rules" / "documentation-agents.md"
    rule_file.write_text("custom")

    result = runner.invoke(main, ["add-doc", "agents", str(tmp_path), "--force"])
    assert result.exit_code == 0
    assert rule_file.read_text() != "custom"
