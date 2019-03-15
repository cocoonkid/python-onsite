'''
Write a script that takes a user inputted string
and prints it out in the following three formats.
    - All letters capitalized.
    - All letters lower case.
    - All vowels lower case and all consonants upper case.

'''

vowel = ["a","e","i","o","u"]


text = input("Please enter a string: ")


text_capitalized = text.upper()

text_lower = text.lower()

print(text_capitalized)

print(text_lower)

counter = 0

for element in vowel:
    list(text)
    if element == text[counter]:
        text[counter].upper()
        counter += 1
print(text)

