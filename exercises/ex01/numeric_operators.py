"""Practicing numeric operators, type conversions, and string concatenation."""
__author__: str = input(730332719)

left_side = input("Left-hand side: ")
right_side = input("Right-hand side: ")
int_left_side = int(left_side)
int_right_side = int(right_side)
exponent = str(int_left_side**int_right_side)
division = str(int_left_side / int_right_side)
int_division = str(int_left_side // int_right_side)
remain = str(int_left_side % int_right_side)
print(left_side + " ** " + right_side + " is " + exponent)
print(left_side + " / " + right_side + " is " + division)
print(left_side + " // " + right_side + " is " + int_division)
print(left_side + " % " + right_side + " is " + remain)