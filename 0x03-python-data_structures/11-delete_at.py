#!/usr/bin/python3
# 11-delete_at.py

"I must apologise PinkPanthress"

def delete_at(my_list=[], idx=0):
    """Delete a ting at a specific place in a list."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
