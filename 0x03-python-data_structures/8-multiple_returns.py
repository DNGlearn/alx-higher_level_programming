#!/usr/bin/python3
# 8-multiple_returns.py

"bruhh hella wavey"

def multiple_returns(sentence):
    """Returns the length of a string and the first char."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
