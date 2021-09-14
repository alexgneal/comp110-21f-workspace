"""Finding duplicate letters in a word."""

__author__ = "730332719"

word: str = input("Enter a word: ")
duplicate: bool = False

i: int = 0
while i < len(word):
    char = word[i]
    j: int = 0 
    while j < len(word):
        if word[j] == char:
            duplicate = True
        else: 
            duplicate = False
        j += 1
    i += 1
print("Found duplicate: " + str(duplicate))