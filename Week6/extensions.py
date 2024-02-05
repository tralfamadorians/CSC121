"""6-12. Extensions: We’re now working with examples that are complex enough

that they can be extended in any number of ways. Use one of the example pro-
grams from this chapter, and extend it by adding new keys and values, chang-
ing the context of the program, or improving the formatting of the output."""

users = {
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    'fact': 'Scientists know him for revolutionizing physics with his general theory of relativity.'
    },

    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    'fact': '''She is remembered for her discovery of radium and polonium, 
            and her huge contribution to finding treatments for cancer.'''
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    print(f"\tMajor discovery: {user_info['fact']}")