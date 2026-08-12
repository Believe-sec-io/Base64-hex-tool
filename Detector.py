import base64
import binascii
import re


def is_hex(text: str) -> bool:
    """Check whether the text contains a valid hexadecimal string."""
    text = text.strip()

    if not text or len(text) % 2 != 0:
        return False

    return bool(re.fullmatch(r"[0-9a-fA-F]+", text))


def is_base64(text: str) -> bool:
    """Check whether the text is valid Base64."""
    text = text.strip()

    if not text:
        return False

    # Base64 normally contains groups of 4 characters.
    if len(text) % 4 != 0:
        return False

    if not re.fullmatch(r"[A-Za-z0-9+/]*={0,2}", text):
        return False

    try:
        base64.b64decode(text, validate=True)
        return True
    except (ValueError, binascii.Error):
        return False


def detect_encoding(text: str) -> str:
    """
    Detect the most likely encoding used by the input.
    Returns:
        BASE64
        HEX
        PLAIN_TEXT
        UNKNOWN
    """

    text = text.strip()

    if not text:
        return "UNKNOWN"

    # Check HEX first.
    if is_hex(text):
        return "HEX"

    # Then check Base64.
    if is_base64(text):
        return "BASE64"

    # If it is readable text, classify it as plain text.
    if all(char.isprintable() or char in "\n\r\t" for char in text):
        return "PLAIN_TEXT"

    return "UNKNOWN"
