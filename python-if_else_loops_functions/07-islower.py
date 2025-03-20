# Write a function that checks for lowercase character.
#
# Prototype: def islower(c):
# Returns True if c is lowercase
# Returns False otherwise
# You are not allowed to import any module
# You are not allowed to use str.upper() and str.isupper()
# Tips: ord()

def islower(c):
    return ord('a') <= ord(c) <= ord('z')

# ord(c) gets the ASCII value of the character c.
# ord('a') (97) and ord('z') (122) define the ASCII range for lowercase letters.
# Checks if c falls within that range → If true, it returns True, otherwise False.
