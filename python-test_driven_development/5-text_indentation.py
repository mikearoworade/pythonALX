# Write a function that prints a text with 2 new lines after each of these characters: ., ? and :
#
# Prototype: def text_indentation(text):
# text must be a string, otherwise raise a TypeError exception with the message text must be a string
# There should be no space at the beginning or at the end of each printed line

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1  # Skip spaces after punctuation
        i += 1

    print(result.strip())
