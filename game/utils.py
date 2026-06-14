from collections.abc import Sequence
from typing import Any


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
