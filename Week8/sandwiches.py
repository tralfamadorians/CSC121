'''8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sand-
wich that’s being ordered. Call the function three times, using a different num-
ber of arguments each time.'''

def sandwich(*toppings):
    # Prints list of sandwich toppings
    print("Sandwich items:")
    for topping in toppings:
        print(topping)
    print("\n")

sandwich('ham', 'cheddar', 'pickles')
sandwich('american cheese', 'mozzarella')
sandwich('pastrimi', 'sauerkraut', 'thousand island')