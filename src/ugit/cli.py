"""Command-line interface for ugit."""

from pathlib import Path

import click

from . import data


@click.group()
def cli() -> None:
    """ugit CLI."""


@cli.command()
def init() -> None:
    """Initialize a new repository."""
    data.init()


@cli.command()
@click.argument("filename", type=click.Path(exists=True, dir_okay=False, readable=True))
def hash_object(filename: str) -> None:
    """
    Hash and store the contents of a file.

    Args:
        filename (str): Path to the file to hash.
    """
    if not Path(".ugit").is_dir():
        click.echo(
            "Error: No .ugit repository found in the current directory.", err=True
        )
    with open(filename, "rb") as file:
        data.hash_object(file.read())
