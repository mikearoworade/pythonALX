# Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
#
# Print all the letters except q and e
# You can only use one print function with string format
# You can only use one loop in your code
# You are not allowed to store characters in a variable
# You are not allowed to import any module

print("".join(f"{chr(i)}" for i in range(97, 123) if i not in (ord('q'), ord('e'))), end="")

# chr(i) converts ASCII values to characters.
# range(97, 123) generates ASCII values for lowercase letters ('a' to 'z').
# List comprehension (f"{chr(i)}" for i in range(97, 123)) creates a string of all letters.
# The if i not in (ord('q'), ord('e')) condition ensures 'q' and 'e' are skipped.
# "".join(...) ensures everything is printed as one continuous string.
# end="" prevents a newline after the output.
print()

for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
