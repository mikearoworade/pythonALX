# Write a function that returns a list with all values multiplied by a number without using
# any loops.
#
# Prototype: def multiply_list_map(my_list=[], number=0):
# Returns a new list:
# Same length as my_list
# Each value should be multiplied by number
# Initial list should not be modified
# You are not allowed to import any module
# You have to use map
# Your file should be max 3 lines

def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))

# map() applies a function to each element in my_list.
# The lambda function multiplies each element by number.
# list() converts the map object back to a list.
