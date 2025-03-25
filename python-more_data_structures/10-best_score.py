# Write a function that returns a key with the biggest integer value.
#
# Prototype: def best_score(a_dictionary):
# You can assume that all values are only integers
# If no score found, return None
# You can assume all students have a different score

def best_score(a_dictionary):
    if not a_dictionary:  # Check if dictionary is empty or None
        return None
    return max(a_dictionary, key=a_dictionary.get)  # Find key with the highest value
