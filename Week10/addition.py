'''10-6. Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a ValueError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.'''

# Ask user for two numbers
number1 = input("Please input a number: ")
number2 = input("Please input a second number: ")

# Print sum and give error if either is not a number
try:
    print(f"The sum of the two numbers are {int(number1) + int(number2)}.")
except ValueError:
    print("Both of your inputs were not numbers.")