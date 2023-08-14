#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rw in matrix:
        for col in rw:
            print("{:d}".format(col), end=" " if col != rw[-1] else "")
        print()
