# Write a function that deletes keys with a specific value in a dictionary.
#
# Prototype: def complex_delete(a_dictionary, value):
# If the value doesn’t exist, the dictionary won’t change
# All keys having the searched value have to be deleted

def complex_delete(a_dictionary, value):
    keys_to_delete = [key for key in a_dictionary if a_dictionary[key] == value]
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary
