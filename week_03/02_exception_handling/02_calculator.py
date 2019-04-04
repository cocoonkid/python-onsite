'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''


num_1 = input("Please enter numbers one:\n")
num_2 = input("Please enter numbers two:\n")


try:
quotient = num_1 / num_2    

