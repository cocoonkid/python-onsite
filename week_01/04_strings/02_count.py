'''
There is a string method called 'count' that is similar to the following
code:

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

Read the documentation of the 'count' method and write an invocation that
counts the number of a’s in 'banana' that uses the in-built 'count'.


'''

text = "banana"

count = text.count("a")
print(count)