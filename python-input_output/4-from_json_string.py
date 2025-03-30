import json

def from_json_string(my_str):
    """Returns a Python object represented by a JSON string."""
    return json.loads(my_str)

# Uses the json module:
# The json.loads() function converts a JSON-formatted string into a Python object.
#
# Returns a Python object:
# Works with JSON representations of lists, dictionaries, numbers, strings, etc.
