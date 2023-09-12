#!/usr/bin/python3
""" Defines the function pascal_triangle """


def pascal_triangle(n):
    """ function returns a list of lists of integers """
    if n <= 0:
        return []

    triang = [[1]]
    while len(triang) != n:
        tri = triang[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        triang.append(temp)
    return triang
