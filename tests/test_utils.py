import pytest

from utils import all_present, all_equal, all_present_and_equal


@pytest.mark.parametrize("collection, expected", [
    ((1, 2, None), False),
    ((None,), False),
    ((0, 0, 0), True),
    (("a", 1, "None"), True),
])
def test_all_present(collection, expected):
    assert all_present(collection) == expected


@pytest.mark.parametrize("collection, expected", [
    ((1, 2, None), False),
    ((None,), True),
    ((None, None, None), True),
    ((0, 0, 0), True),
    (("a", 1, "None"), False),
    (("a", "a", "a"), True),
])
def test_all_equal(collection, expected):
    assert all_equal(collection) == expected


@pytest.mark.parametrize("collection, expected", [
    ((1, 2, 1), False),
    ((None,), False),
    ((1,), True),
    ((None, None, None), False),
    ((0, 0, 0), True),
    (("a", 1, "None"), False),
    (("a", "a", "a"), True),
])
def test_all_present_and_equal(collection, expected):
    assert all_present_and_equal(collection) == expected
