'''10-7. Addition Calculator: Wrap your code from Exercise 10-5 in a while loop
so the user can continue entering numbers, even if they make a mistake and
enter text instead of a number.'''

# Ask user for two numbers
number1 = input("Please input a number: ")
number2 = input("Please input a second number: ")

while not number1.isdigit():
    try:
        number1 = int(number1)
    except ValueError:
        print(f"{number1} is not a number.")

while not number2.isdigit():
    try:
        number2 = int(number1)
    except ValueError:
        print(f"{number2} is not a number.")

# Print sum 
print(f"The sum of the two numbers are {int(number1) + int(number2)}.")



