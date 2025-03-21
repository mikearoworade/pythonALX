# Write a function that prints all integers of a list.
#
# Prototype: def print_list_integer(my_list=[]):
# You can assume that the list only contains integers
# You are not allowed to cast integers into strings
# You have to use str.format() to print integers

def print_list_integer(my_list=[]):
    for num in my_list:
        print("{:d}".format(num))
