def class_to_json(obj):
    """Returns the dictionary description of an object for JSON serialization"""
    return obj.__dict__

# Explanation:
# The __dict__ attribute of an object returns a dictionary of all its attributes.
# This works for objects whose attributes are simple data structures (list, dict, str, int, bool).
# Since JSON can only serialize basic data types, this function ensures compatibility.
