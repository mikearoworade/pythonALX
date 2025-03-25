# Write a class Square that defines a square by: (based on 1-square.py)
#
# Private instance attribute: size
# Instantiation with optional size: def __init__(self, size=0):
# size must be an integer, otherwise raise a TypeError exception with the message size
# must be an integer
# if size is less than 0, raise a ValueError exception with the message size must be >= 0

# Here's the Square class with validation for the size attribute
class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize a square with a private size attribute.

        Args:
            size (int): The size of the square, default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size  # Private instance attribute
