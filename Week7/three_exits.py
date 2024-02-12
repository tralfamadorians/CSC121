'''7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.'''

# Exit with conditional test
more = True
while more == True:
    topping = input("What topping would you like?\nType 'quit' when you're done. ")
    if topping == 'quit':
        more = False
    else:
        print(f"We'll add {topping} to your pizza.")

# Exit with break.
while True:
    topping = input("What topping would you like?\nType 'quit' when you're done. ")
    if topping == 'quit':
        break
    else:
        print(f"We'll add {topping} to your pizza.")


# Exit with active variable.
number = 0
while number < 5:
    topping = input("What topping would you like?\nType 'quit' when you're done. ")
    number += 1
    if topping == 'quit':
        break
    else:
        print(f"We'll add {topping} to your pizza.")