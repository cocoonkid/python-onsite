'''
There are many string methods available to perform all sorts of tasks.

Experiment with some of them to make sure you
understand how they work. strip and replace are particularly useful.

Python documentation uses a syntax that might be confusing.
For example, in find(sub[, start[, end]]), the brackets indicate
optional arguments. So sub is required, but start is optional, and if
you include start, then end is optional.

For this exercise, demonstrate the following string methods below:
- strip
- replace
- find

'''


text = "Hello my name is Franz"

text = text.strip("Hello")

text = text.replace("name", "surname")

text_found = text.find("Franz")

print(text)
print(text_found)