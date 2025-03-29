# Here's the implementation of the MyInt class that inherits from int
# but inverts the == and != operators:

class MyInt(int):
    """A rebellious integer class that inverts == and != operators."""

    def __eq__(self, other):
        """Override == operator to behave like !=."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != operator to behave like ==."""
        return super().__eq__(other)
