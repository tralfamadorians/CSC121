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