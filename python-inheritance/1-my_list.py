# Here's the implementation of the MyList class that inherits from list
# and includes a print_sorted method:

class MyList(list):
    def print_sorted(self):
        print(sorted(self))

# Explanation:
# MyList inherits from list, so it has all the functionalities of a list.
#
# print_sorted(self) prints the list in ascending order using sorted(self),
# which returns a sorted copy of the list without modifying the original list.
