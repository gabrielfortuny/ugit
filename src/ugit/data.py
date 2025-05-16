"""Core data operations."""

from hashlib import sha256
from pathlib import Path

REPO_PATH = Path(".ugit")
OBJECTS_PATH = REPO_PATH / "objects"


def init() -> None:
    """Initialize a new repository."""
    try:
        REPO_PATH.mkdir()
        print(f"Directory '{REPO_PATH}' created successfully.")
        OBJECTS_PATH.mkdir()
        print(f"Directory '{OBJECTS_PATH}' created successfully.")
    except FileExistsError as e:
        print(f"Directory or file '{e.filename}' already exists.")
    except PermissionError as e:
        print(f"Permission denied: Unable to create '{e.filename}'.")


def hash_object(data: bytes) -> None:
    """
    Hashes the given data using SHA-256 and stores it as an object.

    Args:
        data (str): The data to be hashed and stored.

    Returns:
        str: The SHA-256 hexadecimal hash of the data, used as the object ID.
    """
    object_id = sha256(data).hexdigest()
    object_path = OBJECTS_PATH / object_id
    with open(object_path, "wb") as out:
        out.write(data)
    print(f"Hashed object id: {object_id}")
