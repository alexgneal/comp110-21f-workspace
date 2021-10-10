"""List utility functions part 2."""

__author__ = "123456789"

# Define your functions below


def only_evens(numbers: list[int]) -> list[int]:
    """Return the even integers in a list."""
    even_numbers: list[int] = list()
    for number in numbers: 
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Return a list starting at a given index and ending with the end index -1."""
    new_list: list[int] = list()
    if end > len(a_list):
        end = len(a_list)
    if start < 0: 
        start = 0
    while start < end:
        new_list.append(a_list[start])
        start += 1
    return new_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Combine two lists."""
    for i in list_2:
        list_1.append(i)
    return list_1