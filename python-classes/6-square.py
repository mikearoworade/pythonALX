# Write a class Square that defines a square by: (based on 5-square.py)
#
# Private instance attribute: size:
# property def size(self): to retrieve it
# property setter def size(self, value): to set it:
# size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
# if size is less than 0, raise a ValueError exception with the message size must be >= 0
# Private instance attribute: position:
# property def position(self): to retrieve it
# property setter def position(self, value): to set it:
# position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the
# message position must be a tuple of 2 positive integers
# Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
# Public instance method: def area(self): that returns the current square area
# Public instance method: def my_print(self): that prints in stdout the square with the character #:
# if size is equal to 0, print an empty line
# position should be use by using space - Don’t fill lines by spaces when position[1] > 0

class Square:
    """Class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with size and position.

        Args:
            size (int): The size of the square, default is 0.
            position (tuple): The position (x, y) of the square, default is (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size  # Calls the size setter
        self.position = position  # Calls the position setter

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): A tuple of two positive integers.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if (
                not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the '#' character with respect to position."""
        if self.__size == 0:
            print("")  # Print an empty line if size is 0
            return

        # Print top margin (position[1] represents vertical spacing)
        print("\n" * self.__position[1], end="")

        # Print square with horizontal spacing
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
