def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8) and returns
    the number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

# Explanation:
# Uses the with statement:
# Ensures the file is properly closed after writing.
#
# Opens the file in write mode ("w"):
# Creates the file if it doesn’t exist.
# Overwrites the content if the file already exists.
#
# Writes the text and returns the number of characters written:
# f.write(text) writes the string to the file and returns
# the number of characters.
