'''
Write a script that demonstrates a try/except/else.

'''


num_1 = input("Please enter number one:\n")
num_2 = input("Please enter number two:\n")

try:
    quotient = int(num_1) / int(num_2)
except ZeroDivisionError as error:
    print(error)
    print("The numbers zero is no allowed.\n")
except ValueError as error:
    print(error)
    print("You cannot divide string by integers or vice versa\n")
else:
    print(quotient)
