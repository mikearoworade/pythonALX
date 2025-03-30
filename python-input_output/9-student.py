class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the Student instance."""
        return self.__dict__

# The __init__ method initializes the student with first_name, last_name, and age.
#
# The to_json method returns the dictionary representation of the instance using
# self.__dict__, making it suitable for JSON serialization.
