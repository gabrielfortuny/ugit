"""Command-line interface for ugit."""

import click

from . import data


@click.group()
def cli():
    """ugit CLI."""


@cli.command()
def init():
    """Initialize a new repository."""
    data.init()
