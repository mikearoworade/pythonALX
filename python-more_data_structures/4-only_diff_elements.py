# Write a function that returns a set of all elements present in only one set.
#
# Prototype: def only_diff_elements(set_1, set_2):

def only_diff_elements(set_1, set_2):
    return set_1 ^ set_2  # Using the symmetric difference operator (^)
