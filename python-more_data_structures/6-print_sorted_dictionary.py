# Write a function that prints a dictionary by ordered keys.
#
# Prototype: def print_sorted_dictionary(a_dictionary):
# You can assume that all keys are strings
# Keys should be sorted by alphabetic order
# Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
# Dictionary values can have any type

def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):  # Sort the keys alphabetically
        print("{}: {}".format(key, a_dictionary[key]))  # Print each key-value pair

# sorted(a_dictionary.keys()) sorts the dictionary keys in alphabetical order.
# A for loop iterates through the sorted keys.
# print("{}: {}".format(key, a_dictionary[key])) prints each key and its corresponding value.
