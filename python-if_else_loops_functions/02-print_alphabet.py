# Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
#
# You can only use one print function with string format
# You can only use one loop in your code
# You are not allowed to store characters in a variable
# You are not allowed to import any module

print("".join(f"{chr(i)}" for i in range(97, 123)), end="")
print()
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
