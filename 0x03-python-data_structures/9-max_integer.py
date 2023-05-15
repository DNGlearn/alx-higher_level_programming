#!/usr/bin/python3
# 9-max_integer.py

"Afterglow Luna Li"

def max_integer(my_list=[]):
    """Find the largest integer in za list."""
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big:
            big = my_list[i]

    return (big)
