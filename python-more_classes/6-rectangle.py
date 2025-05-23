# Here's the updated Rectangle class that includes the number_of_instances class attribute:
class Rectangle:
    """Defines a rectangle with width and height, and tracks instances."""

    # Public class attribute to track the number of instances
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment instance count

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle using '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """Return a string representation for recreating the object."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when the rectangle instance is deleted and decrement instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement instance count
