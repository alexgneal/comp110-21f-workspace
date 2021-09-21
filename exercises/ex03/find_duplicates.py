"""Finding duplicate letters in a word."""

__author__ = "730332719"

word: str = input("Enter a word: ")
duplicate: bool = False

i: int = 0
j: int = 0

while i < len(word):
    char = word[i]
    j = i + 1
    while j < len(word):
        if word[j] == char:
            duplicate = True
            j = j + 1
        else:
            j = j + 1
    i += 1
print("Found duplicate: " + str(duplicate))