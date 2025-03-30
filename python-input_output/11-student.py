class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)

# __init__: Initializes the Student object with first_name, last_name, and age.
#
# to_json:
# If attrs is a list of strings, it only returns the specified attributes.
# Otherwise, it returns all attributes.

# reload_from_json: Updates the instance attributes using values from a dictionary (json).]
