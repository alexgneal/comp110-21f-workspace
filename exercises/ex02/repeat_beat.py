"""Repeating a beat in a loop."""

__author__ = "730332719"


# Begin your solution here...

user_beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))


i: int = 0
beat: str = ""
while i < repeat:
    beat = ((user_beat + " ") * repeat)
    i = i + 1

if repeat <= 0:
    print("No beat...")

print(beat)