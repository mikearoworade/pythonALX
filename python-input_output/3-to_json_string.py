import json

def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)."""
    return json.dumps(my_obj)

# Uses the json module:
# The json.dumps() function converts a Python object into a JSON-formatted string.
#
# Returns the JSON string representation of my_obj:
# Works with various Python objects like lists, dictionaries, strings, numbers, etc.
