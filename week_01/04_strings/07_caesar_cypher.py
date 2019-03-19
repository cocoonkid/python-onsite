'''
A Caesar cypher is a weak form of encryption that involves “rotating”
each letter by a fixed number of places. To rotate a letter means to
shift it through the alphabet, wrapping around to the beginning if
necessary, so ’A’ rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’.

To rotate a word, rotate each letter by the same amount. For example,
“cheer” rotated by 7 is “jolly” and “melon” rotated by -10 is “cubed”.
In the movie 2001: A Space Odyssey, the ship computer is called HAL,
which is IBM rotated by -1.

Write a function called rotate_word that takes a string and an integer
as parameters, and returns a new string that contains the letters from
the original string rotated by the given amount.

You might want to use the built-in function ord, which converts a
character to a numeric code, and chr, which converts numeric codes to
characters. Letters of the alphabet are encoded in alphabetical order,
so for example:

>>> ord('c') - ord('a')
2

Because 'c' is the two-eth letter of the alphabet. But beware:
the numeric codes for upper case letters are different.

Potentially offensive jokes on the Internet are sometimes encoded in
ROT13, which is a Caesar cypher with rotation 13. If you are not easily
offended, find and decode some of them.

'''

# cheer” rotated by 7 is “jolly” and “melon” rotated by -10 is “cubed”.


# Generating list to hold lower alphabet
alphabet_lower_list = []

# Populating lower alphabet list
alphabet_lower = "a"
for i in range(0, 26):
    alphabet_lower_list.append(alphabet_lower)
    alphabet_lower = chr(ord(alphabet_lower) + 1)


# Generating list to hold upper alphabet
alphabet_upper_list = []

# Populating upper alphabet list
alphabet_upper = "A"
for i in range(0, 26):
    alphabet_upper_list.append(alphabet_upper)
    alphabet_upper = chr(ord(alphabet_upper) + 1)

# Generating list to hold result and lists of alphabet indices per character
rotated_list = []
alphabet__lower_list_indices = []
alphabet_upper_list_indices = []


# Populate lower alphabet indices list
for element in alphabet_lower_list:
    alphabet__lower_list_indices.append(str(alphabet_lower_list.index(element)))


# Populate upper alphabet indices list
for element in alphabet_upper_list:
    alphabet_upper_list_indices.append(str(alphabet_upper_list.index(element)))






# Defining the function for character rotation
def rotate_word(a, b):
    for letter in a:
        # Nesting code into upper or lower alphabets
        if letter == letter.lower():
            position = alphabet_lower_list.index(letter)
            # Nesting code to handle cases outside of indices(0-25) range
            if position + b > 25:
                position = 24 - (position - b)
                rotated_list.append(alphabet_lower_list[position])
                reverse = ord(letter) + b
                rotated_list.append(chr(reverse))

            elif position + b < 0:
                position = 25 - (position - b)
                rotated_list.append(alphabet_lower_list[position])
                reverse = ord(letter) + b
                rotated_list.append(chr(reverse))


            else:
                reverse = ord(letter) + b
                rotated_list.append(chr(reverse))



        elif letter == letter.upper():
            position = alphabet_upper_list.index(letter)

            if position + b > 25:
                position = 24 - (position - b)
                rotated_list.append(alphabet_upper_list[position])
                reverse = ord(letter) + b
                rotated_list.append(chr(reverse))


            elif position + b < 0:
                position = 26 - (position - b)
                rotated_list.append(alphabet_upper_list[position])
                reverse = ord(letter) + b
                rotated_list.append(chr(reverse))

            else:
                reverse = ord(letter) + b
                rotated_list.append(chr(reverse))









rotate_word("melon",-10)

for i in rotated_list:
     print(i, end = " " )



# If (position + b) > index25 change position to index25 -  (b non-negative -position)
#
#
# elif (position + b) < index0 change position to index25 -  (b non-negative -position)

