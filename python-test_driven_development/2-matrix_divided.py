#!/usr/bin/python3
"""This module provides a function to divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float) to divide by.

    Returns:
        A new matrix with all elements divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                  or if rows have different sizes,
                  or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if (not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)

    if not matrix or not all(row for row in matrix):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            try:
                new_num = round(num / div, 2)
                if str(new_num) in ('inf', '-inf', 'nan'):
                    new_num = 0.0
                new_row.append(new_num)
            except (ValueError, OverflowError):
                new_row.append(0.0)
        new_matrix.append(new_row)

    return new_matrix
