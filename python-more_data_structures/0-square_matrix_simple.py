# Write a function that computes the square value of all integers of a matrix.
#
# Prototype: def square_matrix_simple(matrix=[]):
# matrix is a 2 dimensional array
# Returns a new matrix:
# Same size as matrix
# Each value should be the square of the value of the input
# Initial matrix should not be modified

def square_matrix_simple(matrix=[]):
    return [[num ** 2 for num in row] for row in matrix]
