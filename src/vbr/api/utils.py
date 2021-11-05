import uuid

__all__ = ["generate_guid"]


def generate_guid() -> str:
    """Generate a GUID."""
    return str(uuid.uuid4()).upper()
