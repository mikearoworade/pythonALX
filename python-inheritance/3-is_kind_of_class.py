# Write a function that returns True if the object is an instance of,
# or if the object is an instance of a class that inherited from, the
# specified class ; otherwise False.
#
# Prototype: def is_kind_of_class(obj, a_class):

def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class)

# Explanation:
# isinstance(obj, a_class) checks if:
#
# obj is an instance of a_class, or
#
# obj is an instance of a subclass that inherited from a_class.
