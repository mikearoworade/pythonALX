# Write a function that prints all integers of a list, in reverse order.
#
# Prototype: def print_reversed_list_integer(my_list=[]):
# Format: one integer per line. See example
# You are not allowed to import any module
# You can assume that the list only contains integers

def print_reversed_list_integer(my_list=[]):
    if my_list:
        for num in reversed(my_list):
            print("{:d}".format(num))

# First, check if my_list is not None to avoid errors.
# Use reversed(my_list) to iterate over the list in reverse order.
# Print each integer using "{:d}".format(num) to ensure proper formatting.
