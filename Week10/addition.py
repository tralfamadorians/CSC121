
# Ask user for two numbers
number1 = input("Please input a number: ")
number2 = input("Please input a second number: ")

# Print sum and give error if either is not a number
try:
    print(f"The sum of the two numbers are {int(number1) + int(number2)}.")
except ValueError:
    print("Both of your inputs were not numbers.")