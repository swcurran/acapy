"""Wallet utility functions."""

import base58
import base64


def b64_to_bytes(val: str, urlsafe=False) -> bytes:
    """Convert a base 64 string to bytes."""
    if urlsafe:
        return base64.urlsafe_b64decode(val)
    return base64.b64decode(val)


def b64_to_str(val: str, urlsafe=False, encoding=None) -> str:
    """Convert a base 64 string to string on input encoding (default utf-8)."""
    return b64_to_bytes(val, urlsafe).decode(encoding or "utf-8")


def bytes_to_b64(val: bytes, urlsafe=False) -> str:
    """Convert a byte string to base 64."""
    if urlsafe:
        return base64.urlsafe_b64encode(val).decode("ascii")
    return base64.b64encode(val).decode("ascii")


def str_to_b64(val: str, urlsafe=False, encoding=None) -> str:
    """Convert a string to base64 string on input encoding (default utf-8)."""
    return bytes_to_b64(val.encode(encoding or "utf-8"), urlsafe)


def set_urlsafe_b64(val: str, urlsafe: bool = True) -> str:
    """Set URL safety in base64 encoding."""
    if urlsafe:
        return val.replace("+", "-").replace("/", "_")
    return val.replace("-", "+").replace("_", "/")


def b58_to_bytes(val: str) -> bytes:
    """Convert a base 58 string to bytes."""
    return base58.b58decode(val)


def bytes_to_b58(val: bytes) -> str:
    """Convert a byte string to base 58."""
    return base58.b58encode(val).decode("ascii")
