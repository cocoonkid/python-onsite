'''
Write a program that reads in the file words.txt and prints only the
words with more than 20 characters (not counting whitespace).

Source: http://greenteapress.com/thinkpython2/html/thinkpython2010.html

'''

fin= open("words.txt")

for element in fin:
    word = element.rstrip()
    counter = 0
    for element in word:
        counter += 1
        if counter > 20:
            print(word)


