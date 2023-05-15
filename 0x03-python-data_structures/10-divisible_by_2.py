#!/usr/bin/python3
# 10-divisible_by_2.py

"Woman Doja Cat"

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in da list bruhh."""
    multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)
