# Write a function that replaces an element in a list at a specific position without
# modifying the original list (like in C).
#
# Prototype: def new_in_list(my_list, idx, element):
# If idx is negative, the function should return a copy of the original list
# If idx is out of range (> of number of element in my_list), the function should return
# a copy of the original list

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]

    new_list = my_list[:]
    new_list[idx] = element
    return new_list

# If idx is negative or out of range, return a copy of the original list using my_list[:].
# Create a copy of my_list (new_list[:]) to avoid modifying the original list.
# Modify the element at the specified idx in the new list.
# Return the modified copy.
