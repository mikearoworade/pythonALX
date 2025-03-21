# Write a program that prints #pythoniscool, followed by a new line, in the standard output.
#
# Your program should be maximum 2 lines long
# You are not allowed to use print or eval or open or import sys in your file 7-easy_print.py

__import__('os').write(1, b"#pythoniscool\n")

# __import__('os') dynamically imports the os module.
# os.write(1, b"#pythoniscool\n") writes the string to standard output (1 refers to stdout).
# b"#pythoniscool\n" ensures the string is treated as bytes, which is required for os.write.
