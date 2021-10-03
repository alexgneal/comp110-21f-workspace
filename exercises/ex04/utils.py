"""List utility functions."""

__author__ = "730332719"


# TODO: Implement your functions here.


def all(my_list: list[int], number: int) -> bool:
    """Compare one number to each index in a list."""
    index: int = len(my_list) - 1
    while index >= 0:
        if my_list[index] != number:
            return False
        index -= 1
    return True
    

def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Compare two lists."""
    i: int = 0
    while i < len(list_1):
        if len(list_1) != len(list_2):
            return False
        if list_1[i] != list_2[i]:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Return the maximum of a list of integers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    maximum: int = input[0]
    i: int = 0
    while i < len(input): 
        if input[i] > maximum:
            maximum = input[i]
        i += 1
    return maximum