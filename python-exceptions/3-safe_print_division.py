# Write a function that divides 2 integers and prints the result.
#
# Prototype: def safe_print_division(a, b):
# You can assume that a and b are integers
# The result of the division should print on the finally: section preceded by Inside result:
# Returns the value of the division, otherwise: None
# You have to use try: / except: / finally:
# You have to use "{}".format() to print the result

def safe_print_division(a, b):
    try:
        result = a / b  # Perform division
    except ZeroDivisionError:
        result = None  # Handle division by zero
    finally:
        print("Inside result: {}".format(result))  # Always print result
    return result  # Return the division result
