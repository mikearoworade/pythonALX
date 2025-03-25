# Write a class Square that defines a square by: (based on 0-square.py)
#
# Private instance attribute: size
# Instantiation with size (no type/value verification)
# You are not allowed to import any module

# Here’s the Python code for the Square class with a private instance attribute size:
class Square:
    """Class that defines a square."""

    def __init__(self, size):
        """Initialize a square with a private size attribute."""
        self.__size = size  # Private instance attribute
