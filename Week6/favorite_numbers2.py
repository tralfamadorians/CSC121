favorite_number = {
    'Kelly' : [2, 4, 19], 
    'Antonio' : [24],
    'Bob' : [43],
    'Sally' : [1, 7],
    'Tony' : [99]
}

for name, numbers in favorite_number.items():
    print(f"{name}:")
    for number in numbers:
        print(number)
    print("\n")