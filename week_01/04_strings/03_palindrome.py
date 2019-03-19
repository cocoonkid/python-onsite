'''
A string slice can take a third index that specifies the “step size”;
that is, the number of spaces between successive characters.
A step size of 2 means every other character; 3 means every third, etc.

>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'

A step size of -1 goes through the word backwards, so the slice [::-1]
generates a reversed string.

Use this idiom to write a much shorter version of the following functions:

------------------------------------------------------------------------

def first(word):
    """Returns the first character of a string."""
    return word[0]

def last(word):
    """Returns the last of a string."""
    return word[-1]

def middle(word):
    """Returns all but the first and last characters of a string."""
    return word[1:-1]

def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

'''








