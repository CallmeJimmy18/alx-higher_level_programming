#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = -10
    if my_list == "":
        return None
    for list in my_list:
        if list > max_int:
            max_int = list
    return max_int
