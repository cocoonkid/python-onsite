'''
Sum up all elements from the nested list of integers below.

'''

list_ = [1, 2, [10, 11], [42, 3], 9]

result = 0

flat_list = []


for element in list_:
    if element == int:
        pass
    else:
        for x in element:
            flat_list.append(x)

print(flat_list)