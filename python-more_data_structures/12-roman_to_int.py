# Create a function def roman_to_int(roman_string): that converts a Roman numeral
# to an integer.
#
# You can assume the number will be between 1 to 3999.
# def roman_to_int(roman_string) must return an integer
# If the roman_string is not a string or None, return 0

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0

    for char in reversed(roman_string):  # Process from right to left
        value = roman_dict.get(char, 0)
        if value < prev_value:
            total -= value  # Subtract smaller value if it's before a larger one
        else:
            total += value  # Otherwise, add the value
        prev_value = value

    return total