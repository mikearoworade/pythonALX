# Write a function that deletes the item at a specific position in a list.
#
# Prototype: def delete_at(my_list=[], idx=0):
# If idx is negative or out of range, nothing change (returns the same list)
# You are not allowed to use pop()

def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        del my_list[idx]  # Removes the element at the given index
    return my_list  # Return the modified list (or the same list if no deletion occurred)
