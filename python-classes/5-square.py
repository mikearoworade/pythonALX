# Write a class Square that defines a square by: (based on 4-square.py)
#
# Private instance attribute: size:
# property def size(self): to retrieve it
# property setter def size(self, value): to set it:
# size must be an integer, otherwise raise a TypeError exception with the message size must
# be an integer
# if size is less than 0, raise a ValueError exception with the message size must be >= 0
# Instantiation with optional size: def __init__(self, size=0):
# Public instance method: def area(self): that returns the current square area
# Public instance method: def my_print(self): that prints in stdout the square with the
# character #:
# if size is equal to 0, print an empty line

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
        self.size = size  # Calls the setter to validate size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the '#' character."""
        if self.__size == 0:
            print("")  # Print an empty line if size is 0
        else:
            for _ in range(self.__size):
                print("#" * self.__size)  # Print each row of the square
