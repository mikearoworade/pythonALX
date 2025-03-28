def copy_list(l):
    return l[:]

# Explanation:
# l[:] creates a shallow copy of the list by slicing the entire list.
#
# This ensures the returned list is a new object with the same contents as l.
#
# This method works for lists containing any type of objects.
