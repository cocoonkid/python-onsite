'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''





while True:
    try:
        num_1 = int(input("Please enter a number:\n"))
        print(num_1)
        break
    except ValueError:
        print("You must enter a number!")



