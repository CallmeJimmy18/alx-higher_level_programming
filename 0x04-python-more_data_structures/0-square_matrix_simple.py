#!/usr/bin/pyhthon3
def square_matrix_simple(matrix=[]):
    squared = matrix.copy()
    for i in range(len(matrix)):
        squared[i] = list(map((lambda x: x ** 2), matrix[i]))
    return squared
