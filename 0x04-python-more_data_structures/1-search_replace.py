#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_list = my_list.copy()
    for i in range(len(my_list)):
        if nw_list[i] == search:
            nw_list[i] = replace
    return nw_list
