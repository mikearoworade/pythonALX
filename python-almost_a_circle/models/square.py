from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square instance"""
        super().__init__(size, size, x, y, id)
        # Call Rectangle constructor with size as width & height

    def __str__(self):
        """Return string representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size (same as width and height)"""
        return self.width  # Since width == height in a square

    @size.setter
    def size(self, value):
        """Setter for size (sets width and height to the same value)"""
        self.width = value  # Uses width's validation from Rectangle
        self.height = value  # Ensures height is also set

    def update(self, *args, **kwargs):
        """Update attributes of Square"""
        if args and len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in ["id", "size", "x", "y"]:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

