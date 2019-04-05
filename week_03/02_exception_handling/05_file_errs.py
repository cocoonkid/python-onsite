'''
Read in the first number from 'integers.txt' and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''


fin = open("integers.txt")


try:
    for i in fin:
        i = i.rstrip("\n")
        i = int(i)
        x = i * 10
        print(x)
except IOError:
    print("There is a problem with the file.")
except ValueError:
    print("The input data is not of consistent type.")

