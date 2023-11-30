#!/usr/bin/python3
"""  finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):

    for val in range(1, len(list_of_integers) - 1):
        if ((val == 0 or list_of_integers[val - 1] <= list_of_integers[val])
            and (val == len(list_of_integers) - 1 or
                 list_of_integers[val] >= list_of_integers[val + 1])):
            return list_of_integers[val]
    return None
