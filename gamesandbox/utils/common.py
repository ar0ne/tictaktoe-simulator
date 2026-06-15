from collections.abc import Sequence
from typing import Any
from urllib.parse import urlparse


def all_present(col: Sequence[Any]) -> bool:
    return not any(
        el is None
        for el in col
    )


def all_equal(col: Sequence[Any], value: Any) -> bool:
    if not col or len(col) < 1:
        raise ValueError("Collection can't be empty")
    return all(
        el == value
        for el in col
    )


def all_present_and_equal(col: Sequence[Any], value: Any) -> bool:
    return all_present(col) and all_equal(col, value)


def is_valid_url(url: str | None) -> bool:
    if not url:
        return False
    try:
        result = urlparse(url)
        # Ensure it has a scheme (http/https/ftp) and a domain name
        return all([result.scheme, result.netloc])
    except ValueError:
        return False