"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730332719"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

# Begin your solution here...
print("Your fortune cookie says...")
phrase = randint(1, 4) 


if phrase == 1:
    print("Today will be a great day for you!")
else:
    if phrase == 2:
        print("There will be lots of money in your future.")
    else:
        if phrase == 3: 
            print("You will get a 4.0 this semester!")
        else: 
            if phrase == 4:
                print("You will find happiness in the place you least expect it soon!") 

print("Now, go spread positive vibes!")  