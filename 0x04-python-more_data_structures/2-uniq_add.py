#!/usr/bin/python3

"What makes you think"
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    num = 0

    for i in uniq_list:
        num += i

    return (num)
