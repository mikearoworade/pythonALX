# Write a function that divides element by element 2 lists.
#
# Prototype: def list_division(my_list_1, my_list_2, list_length):
# my_list_1 and my_list_2 can contain any type (integer, string, etc.)
# list_length can be bigger than the length of both lists
# Returns a new list (length = list_length) with all divisions
# If 2 elements can’t be divided, the division result should be equal to 0
# If an element is not an integer or float:
# print: wrong type
# If the division can’t be done (/0):
# print: division by 0
# If my_list_1 or my_list_2 is too short
# print: out of range
# You have to use try: / except: / finally:

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            # Try to perform division
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except (TypeError, ValueError):
            print("wrong type")
            result = 0
        finally:
            new_list.append(result)  # Append result to new list

    return new_list  # Return the final list
