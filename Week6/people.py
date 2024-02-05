person_0 = {
    'first_name' : 'antonio',
    'last_name' : 'rivera',
    'age' : 49,
    'city' : 'asheville'
}
person_1 = {
    'first_name' : 'karen',
    'last_name' : 'kirkham',
    'age' : 70,
    'city' : 'kingwood'
}
person_2 = {
    'first_name' : 'angelines',
    'last_name' : 'rivera',
    'age' : 53,
    'city' : 'badajoz'
}

people = [person_0, person_1, person_2]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"Full Name: {full_name.title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}\n")