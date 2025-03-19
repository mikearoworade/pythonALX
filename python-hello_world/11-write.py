# Write a Python script that prints exactly
# and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.
#
# Use the function write from the sys module
# You are not allowed to use print
# Your script should print to stderr
# Your script should exit with the status code 1
import sys

sys.stderr.write("and that piece of art is useful - Dora Korpar, 2015-10-19\n")
sys.exit(1)
