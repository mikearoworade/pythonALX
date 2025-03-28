class Rectangle:
    """A class that defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle using print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self.width for _ in range(self.height))

    def __repr__(self):
        """Return a string that recreates the instance using eval()."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print message and decrement instance count when deleting."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the larger area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)

# ✅ Encapsulation with __width and __height
# ✅ Custom getter and setter for width & height with type and value validation
# ✅ Class attributes number_of_instances and print_symbol
# ✅ area() and perimeter() methods
# ✅ String representation methods (__str__ and __repr__)
# ✅ Custom deletion message (__del__)
# ✅ bigger_or_equal() static method to compare rectangles
# ✅ square() class method to create square instances