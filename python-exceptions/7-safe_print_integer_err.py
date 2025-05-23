# Write a function that prints an integer.
#
# Prototype: def safe_print_integer_err(value):
# value can be any type (integer, string, etc.)
# The integer should be printed followed by a new line
# Returns True if value has been correctly printed (it means the value is an integer)
# Otherwise, returns False and prints in stderr the error precede by Exception:
# You have to use try: / except:
# You have to use "{:d}".format() to print as integer

import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return False
