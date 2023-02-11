#!/usr/bin/python3
"""
This divide a matrix
into a given number
and return a new matrix
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix by a divisor.

    :param matrix: a list of lists of integers or floats
    :param div: the number to divide each element of the matrix by
    """
    msg_1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg_2 = "Each row of the matrix must have the same size"
    msg_3 = "division by zero"
    msg_4 = "div must be a number"
    if not isinstance(div, int):
        raise TypeError(msg_4)
    if not matrix or matrix is None:
        raise TypeError(msg_1)
    if div == 0:
        raise ZeroDivisionError(msg_3)
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError(msg_2)
        for y in row:
            if not isinstance(y, (int, float)):
                raise TypeError(msg_1)
    matrix_reloaded = [[round(x / div, 2) for x in ind] for ind in matrix]
    return matrix_reloaded
