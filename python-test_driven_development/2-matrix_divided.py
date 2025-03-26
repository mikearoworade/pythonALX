# Write a function that divides all elements of a matrix.
#
# Prototype: def matrix_divided(matrix, div):
# matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the
# message matrix must be a matrix (list of lists) of integers/floats
# Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message
# Each row of the matrix must have the same size
# div must be a number (integer or float), otherwise raise a TypeError exception with the message
# div must be a number
# div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
# All elements of the matrix should be divided by div, rounded to 2 decimal places
# Returns a new matrix

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix (list of lists) of integers or floats.
        div (int or float): The number by which to divide each element of the matrix.

    Returns:
        list of lists: A new matrix with each element divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is zero.
    """

    # Check if matrix is a list of lists of integers or floats
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    row_length = len(matrix[0]) if matrix else 0
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and round to 2 decimal places
    return [[round(num / div, 2) for num in row] for row in matrix]
