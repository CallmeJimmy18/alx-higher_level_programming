#!/usr/bin/python3
def no_c(my_string):
    cpy = [s for s in my_string if s != 'c' and s != 'C']
    return ("".join(cpy))
