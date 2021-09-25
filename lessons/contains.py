"""Example of a function that processes a list."""

# Define a function named contains 
# We can give two arguments: a needle value we're searching for and a haystack list


def main() -> None:
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kris", names))


def contains(needle: str, haystack: list[str]) -> bool:
    i: int = 0 
    while i < len(haystack): 
        if haystack[i] == needle:
            return True
        i += 1
    return False


# Python Idiom for starting main function
if __name__ == "__main__":
    main()