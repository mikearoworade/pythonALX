# Write a class Square that defines a square by: (based on 4-square.py)
#
# Private instance attribute: size:
# property def size(self): to retrieve it
# property setter def size(self, value): to set it:
# size must be a number (float or integer), otherwise raise a TypeError exception with the
# message size must be a number
# if size is less than 0, raise a ValueError exception with the message size must be >= 0
# Instantiation with size: def __init__(self, size=0):
# Public instance method: def area(self): that returns the current square area
# Square instance can answer to comparators: ==, !=, >, >=, < and <= based on the square area

class Square:
    """A class that defines a square with a size attribute and comparison operators."""

    def __init__(self, size=0):
        """Initialize the square with a given size.

        Args:
            size (int or float): The size of the square (default is 0).

        Raises:
            TypeError: If size is not a number (float or int).
            ValueError: If size is negative.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int or float): The new size of the square.

        Raises:
            TypeError: If value is not a number (float or int).
            ValueError: If value is negative.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Compare two squares for equality (==)."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """Compare two squares for inequality (!=)."""
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __lt__(self, other):
        """Compare if this square is smaller (<) than another."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Compare if this square is smaller or equal (<=) to another."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """Compare if this square is greater (>) than another."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """Compare if this square is greater or equal (>=) to another."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
