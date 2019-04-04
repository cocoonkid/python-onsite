'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''


fin= open("words.txt")
fout = open("words_reverse.txt", "w")
list = []

for element in fin:
    word = element.rstrip()
    list.append(word)
list.reverse()
for word in list:
    word = word + "\n"
    fout.write(word)