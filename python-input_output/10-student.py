class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance.

        If attrs is a list of strings, only attribute names in this list are retrieved.
        Otherwise, all attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

# The __init__ method initializes the student attributes.
#
# The to_json method:
# If attrs is a list of strings, it filters attributes based on the provided list.
# If attrs is not provided or not a list of strings, it returns all attributes.
# It ensures only valid attributes that exist in the object are included.
