"""Practicing relational operators with concantenations and type conversion."""

__author__ = "730332719"

left_side = input("Left-hand side: ")
right_side = input("Right-hand side: ")
int_left_side = int(left_side)
int_right_side = int(right_side)
less_than = str(int_left_side < int_right_side)
greater_equal = str(int_left_side >= int_right_side)
equal = str(int_left_side == int_right_side)
not_equal = str(int_left_side != int_right_side)
print(left_side + " < " + right_side + " is " + less_than)
print(left_side + " >= " + right_side + " is " + greater_equal)
print(left_side + " == " + right_side + " is " + equal)
print(left_side + " != " + right_side + " is " + not_equal)