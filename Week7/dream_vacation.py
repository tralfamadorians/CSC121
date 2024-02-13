'''7-10. Dream Vacation: Write a program that polls users about their dream vaca-
tion. Write a prompt similar to If you could visit one place in the world, where

would you go? Include a block of code that prints the results of the poll.'''

dream_vacations = {}
active = True

while active:
    name = input("What's your name? ")
    vacation = input(f"What's your dream vacation, {name.title()}? ")
    dream_vacations[name] = vacation

    more = input("Would someone else like to share their dream vacation? (yes/no) ")
    
    if more == 'no':
        active = False

for name, vacation in dream_vacations.items():
    print(f"Name: {name.title()}\nDream Vacation: {vacation.title()}\n")