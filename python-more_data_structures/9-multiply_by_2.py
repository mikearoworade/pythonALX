# Write a function that returns a new dictionary with all values multiplied by 2
#
# Prototype: def multiply_by_2(a_dictionary):
# You can assume that all values are only integers
# Returns a new dictionary

# Create a new dictionary with updated values
def multiply_by_2(a_dictionary):
    return {key: value * 2 for key, value in a_dictionary.items()}
