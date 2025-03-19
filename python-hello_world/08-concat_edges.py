# Complete this source code to print object-oriented programming with Python,
# followed by a new line.
#
# You can find the source code here
# You are not allowed to use any loops or conditional statements
# Your program should be exactly 5 lines long
# You are not allowed to create new variables
# You are not allowed to use string literals

#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"

# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
str = str[39:67] + str[107:112]  + str[:6]# Extract "object-oriented programming" and "with"
print(str)
