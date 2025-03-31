from models.base import Base

class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle instance"""
        super().__init__(id)  # Call Base class constructor

        # Assign values using property setters to ensure validation
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # ✅ Width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # ✅ Height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # ✅ X
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # ✅ Y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # ✅ Area Method
    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height



    # ✅ Improved Display Method (Handles x and y)
    def display(self):
        """Prints the rectangle using the `#` character, considering x and y"""
        print("\n" * self.y, end="")  # Print empty lines for vertical offset
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)  # Print spaces for horizontal offset

    # ✅ Overriding __str__ Method
    def __str__(self):
        """Returns string representation of the Rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.x, self.y, self.width, self.height))

    # ✅ Update Method (Handles *args and **kwargs)
    def update(self, *args, **kwargs):
        """Assigns arguments to each attribute using *args or **kwargs"""
        attributes = ["id", "width", "height", "x", "y"]

        # If *args is provided (and not empty), assign values in order
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            # If no *args, use **kwargs to update attributes by key
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

