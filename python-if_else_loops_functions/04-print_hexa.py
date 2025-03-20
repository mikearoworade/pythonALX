# Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal
#
# You can only use one print function with string format
# You can only use one loop in your code
# You are not allowed to store numbers or strings in a variable
# You are not allowed to import any module

for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))

# print("\n".join(f"{i} = {hex(i)}" for i in range(99)))
