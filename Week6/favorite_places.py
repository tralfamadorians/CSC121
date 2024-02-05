favorite_places = {
    'kelly' : ['new zealand', 'iceland', 'spain'],
    'antonio' : ['thailand', 'united states'],
    'allie' : ['france']
}

for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"{name.title()}'s favorite places are: ")
    else:
        print(f"{name.title()}'s favorite place is: ")
    for place in places:
        print(place.title())
    print("\n")