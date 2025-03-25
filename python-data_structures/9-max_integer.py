# Write a function that finds the biggest integer of a list.
#
# Prototype: def max_integer(my_list=[]):
# If the list is empty, return None
# You can assume that the list only contains integers

def max_integer(my_list=[]):
    if not my_list:
        return None  # Return None if the list is empty

    max_num = my_list[0]  # Assume the first element is the largest

    for num in my_list:
        if num > max_num:
            max_num = num  # Update max_num if a bigger number is found

    return max_num
