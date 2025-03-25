# Write a function that replaces all occurrences of an element by another in a new list.
#
# Prototype: def search_replace(my_list, search, replace):
# my_list is the initial list
# search is the element to replace in the list
# replace is the new element

def search_replace(my_list, search, replace):
    return [replace if num == search else num for num in my_list]
