# Write a function that prints an integer with "{:d}".format().
#
# Prototype: def safe_print_integer(value):
# value can be any type (integer, string, etc.)
# The integer should be printed followed by a new line
# Returns True if value has been correctly printed (it means the value is an integer)
# Otherwise, returns False
# You have to use try: / except:
# You have to use "{:d}".format() to print as integer

def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # Try printing the integer using format()
        return True  # Return True if successful
    except (ValueError, TypeError):
        return False  # Return False if value is not an integer
