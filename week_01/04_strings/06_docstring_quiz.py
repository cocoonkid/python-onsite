'''
The following functions are all intended to check whether a string
contains any lowercase letters, but at least some of them are wrong.
For each function, write its docstring to describe what the function
actually does (assuming that the parameter is a string).



'''

def any_lowercase1(s):
    '''The function returns either True or False for each item in the list that is being iterated through.
    But it is returning False even when there is just one existing uppercase letter'''
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    '''The function always returns True since the string 'c' always returns True when calling  islower() '''
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'



def any_lowercase3(s):
    ''' The function returns True whenever there is a existing lowercase character in a given string.'''
    for c in s:
        flag = c.islower()
    return flag




def any_lowercase4(s):
    ''' The function returns True whenever a lowercase character exists in a given string.
     The Function works but is a very convoluted way of achieving this.'''
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    '''The function returns either True or False for each item in the list that is being iterated through.
     But it is returning False even when there is just one existing lowercase letter'''
    for c in s:
        if not c.islower():
            return False
    return True


