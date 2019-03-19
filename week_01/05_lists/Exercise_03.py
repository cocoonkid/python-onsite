'''
Sum up all elements from the nested list of integers below.

'''

list_ = [1, 2, [10, 11], [42, 3], 9]

flat_list = []

for element in list_:
    if (type(element)) is (int):
        flat_list.append(element)
    else:
        for sub_element in element:
            flat_list.append(sub_element)


print(flat_list)