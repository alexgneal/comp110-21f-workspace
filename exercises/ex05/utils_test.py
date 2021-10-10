"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730332719"


def test_only_evens() -> None:
    """Test that only evens eliminates all odd integers."""
    xs: list[int] = [2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_only_evens_empty() -> None:
    """Test that only evens returns an empty list when given an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_odds() -> None:
    """Test that only evens will return an empty list when given a list of only odd integers."""
    xs: list[int] = [1, 3, 5, 7]
    assert only_evens(xs) == []


def test_sub() -> None: 
    """Test that sub will create a list starting at start and ending at end -1."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    start: int = 1
    end: int = 3
    assert sub(xs, start, end) == [2, 3]


def test_sub_empty() -> None: 
    """Test that sub will create an empty list if start is equal to the length of the list."""
    xs: list[int] = [1, 2]
    start: int = 1
    end: int = 1
    assert sub(xs, start, end) == []


def test_sub_start() -> None:
    """Test that sub will start the sublist at 0 if start is negative."""
    xs: list[int] = [1, 2, 3, 4]
    start: int = -1
    end: int = 3
    assert sub(xs, start, end) == [1, 2, 3]


def test_concat() -> None:
    """Test that concat will combine two lists of integers.""" 
    list_1: list[int] = [1, 2, 3]
    list_2: list[int] = [4, 5, 6]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6]


def test_concat_start() -> None:
    """Test that concat will combine two lists if one is empty."""
    list_1: list[int] = []
    list_2: list[int] = [4, 5, 6]
    assert concat(list_1, list_2) == [4, 5, 6]


def test_concat_empty() -> None:
    """Test that concat will combine two empty lists."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []
