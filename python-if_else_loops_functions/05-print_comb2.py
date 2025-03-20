# Write a program that prints numbers from 0 to 99.
#
# Numbers must be separated by ,, followed by a space
# Numbers should be printed in ascending order, with two digits
# The last number should be followed by a new line
# You can only use no more than 2 print functions with string format
# You can only use one loop in your code
# You are not allowed to store numbers or strings in a variable
# You are not allowed to import any module

print(", ".join(f"{i:02d}" for i in range(100)))

# range(100) generates numbers from 0 to 99.
# f"{i:02d}" ensures each number is printed with two digits (e.g., 00, 01, ..., 99).
# ", ".join(...) joins the numbers with , as required.
# Only one print() function is used.
print()

for number in range(100):
    if number == 99:
        print(f"{number}")
    else:
        print("{:02}".format(number), end=", ")
