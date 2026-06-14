from collections.abc import Sequence
from typing import Any


def all_present(col: Sequence[Any]) -> bool:
    return not any(
        el is None
        for el in col
    )


def all_equal(col: Sequence[Any]) -> bool:
    if not col or len(col) < 1:
        raise ValueError("Collection can't be emply")
    return all(
        True if el == col[0] else False
        for el in col
    )


def all_present_and_equal(col: Sequence[Any]) -> bool:
    return all_present(col) and all_equal(col)
