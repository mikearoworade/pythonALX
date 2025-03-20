# Write a program that prints all possible different combinations of two digits.
#
# Numbers must be separated by ,, followed by a space
# The two digits must be different
# 01 and 10 are considered the same combination of the two digits 0 and 1
# Print only the smallest combination of two digits
# Numbers should be printed in ascending order, with two digits
# The last number should be followed by a new line
# You can only use no more than 3 print functions with string format
# You can only use no more than 2 loops in your code
# You are not allowed to store numbers or strings in a variable
# You are not allowed to import any module

print(", ".join(f"{i}{j}" for i in range(10) for j in range(i + 1, 10)))

# range(10) loops from 0 to 9.
# Nested loop (for j in range(i + 1, 10)) ensures:
# i is always smaller than j (to avoid duplicates like 10 when 01 is already printed).
# Unique and ordered combinations (e.g., 01, 02, ..., 89).
# f"{i}{j}" formats the numbers as two-digit pairs.
# ", ".join(...) ensures:
# Numbers are separated by , .
# The last number is automatically followed by a newline.
print()

for i in range(10):
    for j in range(i + 1, 10):
        print(f"{i}{j}", end=", ")
