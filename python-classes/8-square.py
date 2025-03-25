class Square:
    """A class that defines a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a given size and position.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
            TypeError: If position is not a tuple of two positive integers.
        """
        self.size = size
        self.position = position

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
            ValueError: If value is negative.
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
            not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character with respect to position."""
        if self.__size == 0:
            print("")
            return

        # Print new lines for vertical spacing (position[1])
        print("\n" * self.__position[1], end="")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return a string representation of the square, behaving like my_print()."""
        if self.__size == 0:
            return ""

        square_str = "\n" * self.__position[1]  # Vertical spacing
        for _ in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size + "\n"

        return square_str.rstrip()  # Remove trailing newline

# Features of this Class:
# Encapsulation:
# Uses private instance attributes __size and __position.
# Uses property methods size and position with validation.
#
# Validation:
# size must be an integer and ≥ 0.
# position must be a tuple of two positive integers.
#
# Methods:
# area(): Returns the area of the square.
# my_print(): Prints the square with the given position.
# __str__(): Returns a string representation, behaving like my_print().
