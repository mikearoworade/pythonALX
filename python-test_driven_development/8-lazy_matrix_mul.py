# Write a function that multiplies 2 matrices by using the module NumPy
#
# To install it: pip3 install numpy==1.15.0
# Prototype: def lazy_matrix_mul(m_a, m_b):

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        list: The resulting matrix from multiplying m_a by m_b.

    Raises:
        ValueError: If m_a and m_b cannot be multiplied.
    """
    return np.matmul(m_a, m_b)
