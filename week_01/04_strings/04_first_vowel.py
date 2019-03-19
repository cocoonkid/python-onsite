'''
Write a script that finds the first vowel in a a user inputted string.

'''



vowel = ["a","e","i","o","u"]

text = input("Please enter a string: ")


for element in vowel:
    if element in text:
        result = text.find(element)
        print(text[result])
        break
    else:
        print("There is no vowel in this text!")
        break




