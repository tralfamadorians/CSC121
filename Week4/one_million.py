"""4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing CTRL-C or by closing the output window.)"""

million = [number for number in range(1, 1_000_001)]
for number in million:
    print(number)
