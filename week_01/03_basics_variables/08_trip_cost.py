'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''



mtd = input("Please tell me how many miles to drive: ")
mpg = input("Please tell me the average miles per gallon (consumption rate) of your car: ")
price = input("Please tell me the current price per gallon of fuel: ")
cost = float(mtd) * float(mpg) * float(price)

print(f"You'll be driving {mtd} miles with an average rate of consumption of {mpg} gallon per miles and your trip will cost {cost} at an average price of {price} per gallon of fuel!")