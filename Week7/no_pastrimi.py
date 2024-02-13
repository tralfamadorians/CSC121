'''7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.'''

sandwich_orders = ['pastrami', 'ham', 'turkey', 'pastrami', 'cheese', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current = sandwich_orders.pop()
    print(f"I made your {current} sandwich.")
    finished_sandwiches.append(current)

print("\nThe following sandwiches were made:")
for sandwich in finished_sandwiches:
    print(sandwich)