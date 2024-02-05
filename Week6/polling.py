favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people = ['jen', 'sam', 'sarah', 'edward', 'phil', 'pam']

for name in people:
    if name in favorite_languages.keys():
        print(f"Thank you for responding, {name.title()}.")
    else:
        print(f"You are invited to take the poll, {name.title()}.")
