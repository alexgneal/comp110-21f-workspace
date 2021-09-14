"""Drawing forests in a loop."""

__author__ = "730332719"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))

i: int = 0
tree = TREE

if depth > 0:
    while i < depth:
        tree = TREE * (i + 1)
        i = i + 1
        print(tree)
