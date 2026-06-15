import pytest

from game.utils.common import all_present, all_equal, all_present_and_equal


@pytest.mark.parametrize("collection, expected", [
    ((1, 2, None), False),
    ((None,), False),
    ((0, 0, 0), True),
    (("a", 1, "None"), True),
])
def test_all_present(collection, expected):
    assert all_present(collection) == expected


@pytest.mark.parametrize("collection, equal_to, expected", [
    ((1, 2, None), 1, False),
    ((None,), None, True),
    ((None, None, None), None, True),
    ((0, 0, 0), 0, True),
    (("a", 1, "None"), "a", False),
    (("a", "a", "a"), "a", True),
])
def test_all_equal(collection, equal_to, expected):
    assert all_equal(collection, equal_to) == expected


@pytest.mark.parametrize("collection, equal_to, expected", [
    ((1, 2, 1), 1, False),
    ((None,), 1, False),
    ((1,), 1, True),
    ((None, None, None), 1, False),
    ((0, 0, 0), 0, True),
    (("a", 1, "None"), 1, False),
    (("a", "a", "a"), "a", True),
])
def test_all_present_and_equal(collection, equal_to, expected):
    assert all_present_and_equal(collection, equal_to) == expected


def test_all_equal_invalid():
    with pytest.raises(ValueError):
        all_equal(None, "a")

    with pytest.raises(ValueError):
        all_equal([], 1)

    with pytest.raises(ValueError):
        all_equal(tuple(), True)
