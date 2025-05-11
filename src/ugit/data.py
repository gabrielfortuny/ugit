"""Core data operations."""

from .config import REPO_PATH


def init():
    """Initialize a new repository."""
    try:
        REPO_PATH.mkdir()
        print(f"Directory '{REPO_PATH}' created successfully.")
    except FileExistsError:
        print(f"Directory or file '{REPO_PATH}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{REPO_PATH}'.")
