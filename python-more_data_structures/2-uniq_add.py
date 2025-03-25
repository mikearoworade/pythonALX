# Write a function that adds all unique integers in a list (only once for each integer).
#
# Prototype: def uniq_add(my_list=[]):

def uniq_add(my_list=[]):
    return sum(set(my_list))
