# Write a function that prints the first x elements of a list and only integers.
#
# Prototype: def safe_print_list_integers(my_list=[], x=0):
# my_list can contain any type (integer, string, etc.)
# All integers have to be printed on the same line followed by a new line - other type of
# value in the list must be skipped (in silence).
# x represents the number of elements to access in my_list
# x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
# Returns the real number of integers printed
# You have to use try: / except:
# You have to use "{:d}".format() to print an integer

# Here's the function that prints the first x integers from a list while
# skipping non-integer values silently:
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Track the number of integers printed
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end=" ")  # Print integer without newline
            count += 1  # Increase count if successful
        except (ValueError, TypeError):
            continue  # Skip non-integer values
    print()  # Print a new line at the end
    return count  # Return the count of printed integers
