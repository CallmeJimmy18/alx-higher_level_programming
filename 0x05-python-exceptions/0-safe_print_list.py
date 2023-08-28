#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    d = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            d = d + 1
    except Exception:
        pass
    print()
    return d
