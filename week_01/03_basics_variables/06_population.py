'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''



current_pop = 380123456

secondsperyear = 356*24*60*60
secondsperyear = 356*24*60*60
secondsperyear = 356*24*60*60

born = secondsperyear/6
died = secondsperyear/12
immigrants = secondsperyear/40

year1 = current_pop + born - died + immigrants
year2 = year1 + born - died + immigrants
year3 = year2 + born - died + immigrants

print(f"There is a population of {year1} after the first year, a population of {year2} after year 2, and a population of {year3} after year 3.")



