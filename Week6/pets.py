pet_0 = {
    'name' : 'burku',
    'kind' : 'dog',
    'owner' : 'antonio'
}

pet_1 = {
    'name' : 'emma',
    'kind' : 'dog',
    'owner' : 'karen'
}

pet_2 = {
    'name' : 'sam',
    'kind' : 'dog',
    'owner' : 'allie'
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"Name: {pet['name'].title()}")
    print(f"Kind: {pet['kind'].title()}")
    print(f"Owner: {pet['owner'].title()}\n")