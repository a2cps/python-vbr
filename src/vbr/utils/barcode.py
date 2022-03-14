"""For working with strings that can be used as barcode identifiers."""
import re
import uuid

__all__ = ["sanitize_identifier_string", "generate_barcode_string"]


def sanitize_identifier_string(barcode: str, no_spaces=False) -> str:
    """Remove whitespace and other junk characters from a barcode string."""
    if barcode is None:
        return None
    if no_spaces:
        barcode = re.sub(r"\s+", "", barcode)
    barcode = barcode.strip()
    # TODO - add other sanitization rules
    return barcode


def generate_barcode_string(length: int = 12) -> str:
    """Generate a string that can serve as a barcoded identifier.

    Barcodes will begin with V and end with a checksum integer.
    """
    if length < 12:
        raise ValueError("length must be >= 12")
    if length > 25:
        raise ValueError("length must be <= 25")
    barcode = "V" + uuid.uuid4().hex[: (length - 1)].upper()
    checksum = str(sum(bytearray(barcode.encode("utf-8"))) % 10)
    return barcode + checksum
