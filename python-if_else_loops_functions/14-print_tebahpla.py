# Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.
#
# You can only use one print function with string format
# You can only use one loop in your code
# You are not allowed to store characters in a variable
# You are not allowed to import any module

for i in range(122, 96, -1):
    print(f"{chr(i) if i % 2 == 0 else chr(i).upper()}", end="")

# Loop from z (ASCII 122) to a (ASCII 97) in reverse order.
# Use chr(i) to convert ASCII values to characters:
# If i is even, print it as lowercase.
# If i is odd, convert it to uppercase using .upper().
# Use end="" to ensure all characters print on the same line.
