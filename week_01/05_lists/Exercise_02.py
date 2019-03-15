'''
Given the two lists below, find the elements that are the same
and put them in a new list.
Put the elements that are different in another list.

Print both.

'''

list_one = [0, 4, 6, 18, 25, 42, 100]
list_two = [1, 4, 9, 24, 42, 88, 99, 100]


new_list = []
other_list = []


for element in list_one:
    if element in list_two:
        new_list.append(element)

    else:
        other_list.append(element)


for element in list_two:
    if element in list_one:
        pass
    else:
        other_list.append(element)



print(new_list)
print(other_list)
