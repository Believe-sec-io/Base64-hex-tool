import base64


def encode_base64(text: str) -> str:
    """Encode text into Base64."""
    encoded = base64.b64encode(text.encode("utf-8"))
    return encoded.decode("ascii")


def decode_base64(text: str) -> str:
    """Decode Base64 into UTF-8 text."""
    try:
        decoded = base64.b64decode(text, validate=True)
        return decoded.decode("utf-8")
    except Exception as error:
        raise ValueError("Invalid Base64 input.") from error


def encode_hex(text: str) -> str:
    """Encode text into hexadecimal."""
    return text.encode("utf-8").hex()


def decode_hex(text: str) -> str:
    """Decode hexadecimal into UTF-8 text."""
    try:
        decoded = bytes.fromhex(text)
        return decoded.decode("utf-8")
    except Exception as error:
        raise ValueError("Invalid hexadecimal input.") from error
