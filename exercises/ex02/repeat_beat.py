"""Repeating a beat in a loop."""

__author__ = "730332719"


# Begin your solution here...

user_beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))

i: int = 0
beat: str = ""
if repeat > 0:
    while i < repeat:
        beat = ((user_beat + " ") * repeat)
        i = i + 1
    print(beat)
else:
    print("No beat...")