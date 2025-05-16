"""Core data operations."""

from pathlib import Path


def init():
    """Initialize a new repository."""
    repo_path = Path(".ugit")
    objects_path = repo_path / "objects"
    try:
        repo_path.mkdir()
        print(f"Directory '{repo_path}' created successfully.")
        objects_path.mkdir()
        print(f"Directory '{objects_path}' created successfully.")
    except FileExistsError as e:
        print(f"Directory or file '{e.filename}' already exists.")
    except PermissionError as e:
        print(f"Permission denied: Unable to create '{e.filename}'.")
