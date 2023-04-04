#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of list of int/float): The matrix to divide.
        div (int/float): The divisor to use for division.

    Returns:
        list of list of float: A new matrix where all elements have been divided by div and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats or if div is not an integer/float.
        ZeroDivisionError: If div is equal to 0.
        TypeError: If the rows of matrix are not all of the same size.
    """
    # Check that matrix is a list of lists of integers/floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or \
            not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # Check that all rows of matrix are of the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    # Check that div is an integer/float and is not equal to 0
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Divide all elements of matrix by div and round to 2 decimal places
    return [[round(num/div, 2) for num in row] for row in matrix]
