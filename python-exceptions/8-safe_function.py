# Write a function that executes a function safely.
#
# Prototype: def safe_function(fct, *args):
# You can assume fct will be always a pointer to a function
# Returns the result of the function,
# Otherwise, returns None if something happens during the function and prints in stderr
# the error precede by Exception:
# You have to use try: / except:

import sys

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
