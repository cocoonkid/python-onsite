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

temp_list = []

for element in text:
    temp_list.append(element)

for element in temp_list:
    if element in vowel:
        index = temp_list.index(element)
        temp_list[index] = element.lower()
    elif element not in vowel:
        index = temp_list.index(element)
        temp_list[index] = element.upper()

for element in temp_list:
    print(element, end="")












# for element in vowel:
#     if element in text:
#         result = text.find(element)
#         print(text[result])
#         break
#     else:
#         print("There is no vowel in this text!")
#         break