# Write a function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).
#
# Prototype: def remove_char_at(str, n):
# You are not allowed to import any module

def remove_char_at(str, n):
    return str[:n] + str[n+1:] if 0 <= n < len(str) else str

# Check if n is within the valid index range (0 ≤ n < len(str)).
# If n is valid, remove the character at index n by slicing.
# Otherwise, return the string unchanged.
# String slicing technique:
# str[:n] → Gets the part before n.
# str[n+1:] → Gets the part after n.
# Concatenating them removes the n-th character.
