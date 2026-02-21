"""CLI entry point for claude-templates."""

from pathlib import Path

import click

from claude_templates import __version__
from claude_templates.installer import diff_template, install_template
from claude_templates.templates import TEMPLATES, get_template_dir, list_template_files


@click.group()
@click.version_option(version=__version__)
def main():
    """Claude Code project templates."""


@main.command("list")
def list_cmd():
    """List available templates."""
    click.echo()
    click.echo(f"  {'Template':<20} Description")
    click.echo(f"  {'--------':<20} -----------")
    for name, meta in TEMPLATES.items():
        click.echo(f"  {name:<20} {meta['description']}")
    click.echo()


@main.command()
@click.argument("template")
def info(template: str):
    """Show template details and file list."""
    try:
        meta = TEMPLATES[template]
    except KeyError:
        raise click.ClickException(
            f"Unknown template: '{template}'. Run 'claude-templates list' to see options."
        )

    click.echo()
    click.echo(f"  Template:    {template}")
    click.echo(f"  Description: {meta['description']}")
    click.echo()
    click.echo(f"  {meta['details']}")
    click.echo()

    template_files = list_template_files(template)
    if template_files:
        click.echo("  Files:")
        for f in template_files:
            click.echo(f"    {f}")
    click.echo()


@main.command()
@click.argument("template")
@click.argument("path", default=".", type=click.Path())
@click.option("--force", is_flag=True, help="Overwrite existing files without prompting.")
def init(template: str, path: str, force: bool):
    """Apply a template to a project directory."""
    try:
        template_dir = get_template_dir(template)
    except KeyError as e:
        raise click.ClickException(str(e))

    target = Path(path).resolve()
    target.mkdir(parents=True, exist_ok=True)

    if not force:
        _, existing = diff_template(template_dir, target)
        if existing:
            click.echo(f"\n  The following files already exist in {target}:")
            for f in existing:
                click.echo(f"    {f}")
            click.echo()
            if not click.confirm("  Overwrite these files?", default=False):
                click.echo("  Aborted. Use --force to skip this prompt.")
                return

            force = True

    created, skipped = install_template(template_dir, target, force=force)

    click.echo()
    if created:
        click.echo(f"  Created {len(created)} file(s) in {target}:")
        for f in created:
            click.echo(f"    + {f}")
    if skipped:
        click.echo(f"  Skipped {len(skipped)} existing file(s):")
        for f in skipped:
            click.echo(f"    ~ {f}")
    click.echo()
    click.echo(f"  Template '{template}' applied successfully.")
    click.echo()


@main.command()
@click.argument("template")
@click.argument("path", default=".", type=click.Path())
def diff(template: str, path: str):
    """Preview what would change (dry run)."""
    try:
        template_dir = get_template_dir(template)
    except KeyError as e:
        raise click.ClickException(str(e))

    target = Path(path).resolve()
    new, existing = diff_template(template_dir, target)

    click.echo()
    if new:
        click.echo(f"  New files ({len(new)}):")
        for f in new:
            click.echo(f"    + {f}")
    if existing:
        click.echo(f"  Would overwrite ({len(existing)}):")
        for f in existing:
            click.echo(f"    ! {f}")
    if not new and not existing:
        click.echo("  No changes — template already fully applied.")
    click.echo()
