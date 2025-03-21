# Write a program that prints the number of and the list of its arguments.

import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name
    argc = len(argv)

    print("{} argument{}{}"
          .format(argc, "s" if argc != 1 else "", ":" if argc > 0 else "."))

    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))

# Import sys to access sys.argv (which holds command-line arguments).
# Ignore the script name (sys.argv[0]) by slicing sys.argv[1:].
# Count the arguments (argc) using len(argv).
# Print the number of arguments with correct singular/plural formatting:
# "argument" if argc == 1, otherwise "arguments".
# Use : if at least one argument exists, otherwise use ".".
# Iterate through arguments (starting from 1) and print their index and value.
