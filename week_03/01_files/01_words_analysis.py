'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.

Why does the code jump over when I activate the word counter.
'''

from heapq import nlargest, nsmallest


fin = open("words.txt")


## Word Counter
# for element in fin:
#     word_counter = 0
#     word = element.rstrip()
#     for word in fin:
#         word_counter += 1
#     print(word_counter)

## Dict for keeping count of chars per word
lib = {}


## Char Counter
for element in fin:
    word = element.rstrip()
    for word in fin:
        word = word.rstrip("\n")
        char_counter = 0
        for char in word:
            char_counter += 1
            lib[word] = char_counter


largest = nlargest(1, lib, key=lib.get)
smallest = nsmallest(1, lib, key=lib.get)

for element in largest:
    counter = 0
    for char in element:
        counter +=1
    for key, value in lib.items():
        if value == counter:
            print(key)


for element in smallest:
    counter = 0
    for char in element:
        counter += 1
    for key, value in lib.items():
        if value == counter:
            print(key)


