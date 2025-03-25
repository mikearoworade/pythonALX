# Write a function that deletes a key in a dictionary.
#
# Prototype: def simple_delete(a_dictionary, key=""):
# key argument will be always a string

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]  # Remove the key if it exists
    return a_dictionary  # Return the updated dictionary
