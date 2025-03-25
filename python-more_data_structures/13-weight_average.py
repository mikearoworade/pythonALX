# Write a function that returns the weighted average of all integers tuple (<score>, <weight>)
#
# Prototype: def weight_average(my_list=[]):
# Returns 0 if the list is empty

def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weighted_sum = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    return total_weighted_sum / total_weight if total_weight != 0 else 0
