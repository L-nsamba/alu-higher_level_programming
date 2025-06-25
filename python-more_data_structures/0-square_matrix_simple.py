#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Use list comprehension to return a new matrix with squared values
    return [[element ** 2 for element in row] for row in matrix]
