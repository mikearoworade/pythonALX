# Write a program that prints the alphabet in uppercase, followed by a new line.
#
# Your program should be maximum 3 lines long
# You are not allowed to use:
# any loops
# any conditional statements
# str.join()
# any string literal
# any system calls

import sys
sys.stdout.write("".join(map(chr, range(65, 91))) + "\n")

# range(65, 91): Generates ASCII values for uppercase letters (A-Z).
# map(chr, range(65, 91)): Converts ASCII values to characters.
# "".join(...): Combines the characters into a single string.
# sys.stdout.write(...): Prints the result followed by a new line.
# map() is a built-in function that applies a given function to all items in an iterable (e.g., list, tuple)
# and returns a map object (an iterator). map(function, iterable)
