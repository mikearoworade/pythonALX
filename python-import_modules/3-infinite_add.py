# Write a program that prints the result of the addition of all arguments
#
# The output should be the result of the addition of all arguments, followed by a new line
# You can cast arguments into integers by using int() (you can assume that all arguments
# can be casted into integers)
# Your code should not be executed when imported

import sys

if __name__ == "__main__":
    total = sum(int(arg) for arg in sys.argv[1:])
    print(total)

# sys.argv contains command-line arguments as strings.
# sys.argv[1:] excludes the script name (sys.argv[0]).
# int(arg) for arg in sys.argv[1:] converts each argument to an integer.
# sum(...) computes the total sum.
# if __name__ == "__main__": ensures the script only runs when executed directly.
