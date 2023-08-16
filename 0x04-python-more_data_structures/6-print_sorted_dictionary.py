#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_dictlis = list(a_dictionary.keys())
    my_dictlis.sort()
    sort_dict = {i: a_dictionary[i] for i in my_dictlis}
    for x, z in sort_dict.items():
        print("{}: {}".format(x, z))
