# Write a function that prints a string in uppercase followed by a new line.
#
# Prototype: def uppercase(str):
# You can only use no more than 2 print functions with string format
# You can only use one loop in your code
# You are not allowed to import any module
# You are not allowed to use str.upper() and str.isupper()
# Tips: ord()

def uppercase(str):
    print("".join(chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in str))

# ord(c) - 32: Converts lowercase letters to uppercase (ASCII difference between a and A is 32).
# chr(...): Converts the modified ASCII value back to a character.
# if 'a' <= c <= 'z' else c: Ensures non-lowercase characters remain unchanged.
# "".join(...): Joins all modified characters into a single string.
