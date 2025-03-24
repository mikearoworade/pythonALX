# Write a function that replaces an element of a list at a specific position (like in C).
#
# Prototype: def replace_in_list(my_list, idx, element):
# If idx is negative, the function should not modify anything, and returns the original list
# If idx is out of range (> of number of element in my_list), the function should not modify
# anything, and returns the original list

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the original list if idx is out of range
    my_list[idx] = element  # Replace the element at the specified index
    return my_list  # Return the modified list
