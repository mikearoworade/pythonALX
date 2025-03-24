# Write a function that adds 2 tuples.
#
# Prototype: def add_tuple(tuple_a=(), tuple_b=()):
# Returns a tuple with 2 integers:
# The first element should be the addition of the first element of each argument
# The second element should be the addition of the second element of each argument

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements, default missing values to 0
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    return (a1 + b1, a2 + b2)
