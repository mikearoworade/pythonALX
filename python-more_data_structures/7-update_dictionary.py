# Write a function that replaces or adds key/value in a dictionary.
#
# Prototype: def update_dictionary(a_dictionary, key, value):
# key argument will be always a string
# value argument will be any type
# If a key exists in the dictionary, the value will be replaced

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value  # Add or update the key-value pair
    return a_dictionary  # Return the updated dictionary
