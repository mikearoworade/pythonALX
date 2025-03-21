# Write a program that prints all the names defined by the compiled module hidden_4.pyc
#
# You should print one name per line, in alpha order
# You should print only names that do not start with __
# Your code should not be executed when imported

if __name__ == '__main__':
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if not name.startswith('__'):
            print(name)
