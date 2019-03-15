'''
Take in 10 numbers from the user. Place the numbers in a list.
Using the loop of your choice, calculate the sum of all of the
numbers in the list as well as the average.

Print the results.

'''




num = input("Please enter 10 numbers seperated by space: \n")

list_of_num = num.split()

result = 0

for element in list_of_num:
    result += int(element)

print(result)

for element in list_of_num:
    result += int(element)

result = result / len(list_of_num)

print(result)



