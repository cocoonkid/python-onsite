'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''





num_1 = input("Please enter number one:\n")
num_2 = input("Please enter number two:\n")

try:
    quotient = int(num_1) / int(num_2)
    print(quotient)
except ZeroDivisionError as error:
    print(error)
    print("The numbers zero is no allowed.\n")
except ValueError as error:
    print(error)
    print("You cannot divide string by integers or vice versa\n")









# try:
#     if ((int(num_1)) or (int(num_2))) == 0:
# except:
#     print("The number zero is not allowed")
# try:
#     if (num_1 or num_2) == type(str):
# except:
#     print("A string is not allowed")