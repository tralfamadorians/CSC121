tickets = int(input("How many tickets will you be purchasing? "))


total, price = 0, 0

while tickets > 0:
    age = int(input("What is the age of the person who will be using this ticket? "))
    
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15
    
    total += price
    tickets -= 1

print(f"\nThe price of your tickets is ${total}.")