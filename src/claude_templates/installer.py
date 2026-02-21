"""Template installation logic."""

import shutil
from pathlib import Path

GITIGNORE_ENTRIES = [
    "CLAUDE.local.md",
    ".claude/settings.local.json",
]


def install_template(
    template_dir: Path,
    target_dir: Path,
    force: bool = False,
) -> tuple[list[Path], list[Path]]:
    """Copy template files to target directory.

    Returns (created_files, skipped_files) as relative paths.
    """
    created: list[Path] = []
    skipped: list[Path] = []

    for source_file in sorted(template_dir.rglob("*")):
        if source_file.is_dir():
            continue

        relative = source_file.relative_to(template_dir)
        dest = target_dir / relative

        if dest.exists() and not force:
            skipped.append(relative)
            continue

        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, dest)
        created.append(relative)

    ensure_gitignore_entries(target_dir)
    return created, skipped


def diff_template(template_dir: Path, target_dir: Path) -> tuple[list[Path], list[Path]]:
    """Preview what would change. Returns (new_files, existing_files)."""
    new: list[Path] = []
    existing: list[Path] = []

    for source_file in sorted(template_dir.rglob("*")):
        if source_file.is_dir():
            continue

        relative = source_file.relative_to(template_dir)
        dest = target_dir / relative

        if dest.exists():
            existing.append(relative)
        else:
            new.append(relative)

    return new, existing


def ensure_gitignore_entries(target_dir: Path) -> None:
    """Add standard entries to .gitignore if not already present."""
    gitignore = target_dir / ".gitignore"

    existing_lines: set[str] = set()
    if gitignore.exists():
        existing_lines = {line.strip() for line in gitignore.read_text().splitlines()}

    to_add = [entry for entry in GITIGNORE_ENTRIES if entry not in existing_lines]
    if not to_add:
        return

    with gitignore.open("a") as f:
        if existing_lines and "" not in existing_lines:
            f.write("\n")
        f.write("# Claude Code local files\n")
        for entry in to_add:
            f.write(f"{entry}\n")
