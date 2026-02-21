"""Tests for the CLI commands."""

from click.testing import CliRunner

from claude_templates.cli import main


runner = CliRunner()


def test_list_shows_all_templates():
    result = runner.invoke(main, ["list"])
    assert result.exit_code == 0
    assert "coding" in result.output
    assert "analysis" in result.output
    assert "research" in result.output
    assert "data-engineering" in result.output
    assert "writing" in result.output


def test_info_known_template():
    result = runner.invoke(main, ["info", "coding"])
    assert result.exit_code == 0
    assert "coding" in result.output
    assert "DDD" in result.output
    assert "Files:" in result.output


def test_info_unknown_template():
    result = runner.invoke(main, ["info", "nonexistent"])
    assert result.exit_code != 0
    assert "Unknown template" in result.output


def test_init_creates_files(tmp_path):
    result = runner.invoke(main, ["init", "coding", str(tmp_path)])
    assert result.exit_code == 0
    assert "Created" in result.output
    assert (tmp_path / "CLAUDE.md").exists()
    assert (tmp_path / ".claude" / "settings.local.json").exists()
    assert (tmp_path / ".claude" / "rules" / "backend.md").exists()


def test_init_unknown_template(tmp_path):
    result = runner.invoke(main, ["init", "nonexistent", str(tmp_path)])
    assert result.exit_code != 0
    assert "Unknown template" in result.output


def test_init_skips_existing_files(tmp_path):
    # First init
    runner.invoke(main, ["init", "writing", str(tmp_path)])
    # Modify a file
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text("custom content")

    # Second init without --force — answer 'n' to overwrite prompt
    result = runner.invoke(main, ["init", "writing", str(tmp_path)], input="n\n")
    assert "already exist" in result.output
    # File should be unchanged
    assert claude_md.read_text() == "custom content"


def test_init_force_overwrites(tmp_path):
    # First init
    runner.invoke(main, ["init", "writing", str(tmp_path)])
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text("custom content")

    # Second init with --force
    result = runner.invoke(main, ["init", "writing", str(tmp_path), "--force"])
    assert result.exit_code == 0
    assert claude_md.read_text() != "custom content"


def test_diff_shows_new_files(tmp_path):
    result = runner.invoke(main, ["diff", "coding", str(tmp_path)])
    assert result.exit_code == 0
    assert "New files" in result.output
    assert "CLAUDE.md" in result.output


def test_diff_shows_existing_files(tmp_path):
    # Create a file that would conflict
    (tmp_path / "CLAUDE.md").write_text("existing")

    result = runner.invoke(main, ["diff", "coding", str(tmp_path)])
    assert result.exit_code == 0
    assert "Would overwrite" in result.output


def test_diff_unknown_template(tmp_path):
    result = runner.invoke(main, ["diff", "nonexistent", str(tmp_path)])
    assert result.exit_code != 0


def test_version():
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.output
