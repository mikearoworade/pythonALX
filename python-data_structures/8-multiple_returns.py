# Write a function that returns a tuple with the length of a string and its first character.
#
# Prototype: def multiple_returns(sentence):
# If the sentence is empty, the first character should be equal to None

def multiple_returns(sentence):
    if sentence:
        return (len(sentence), sentence[0])
    else:
        return (0, None)
