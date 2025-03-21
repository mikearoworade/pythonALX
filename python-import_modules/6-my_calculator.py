# Write a program that imports all functions from the file calculator_1.py and
# handles basic operations.wer67890-


from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./06-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    if op in operations:
        result = operations[op](a, b)
        print(f"{a} {op} {b} = {result}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
