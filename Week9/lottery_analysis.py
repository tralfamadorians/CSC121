'''9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write
a loop that keeps pulling numbers until your ticket wins. Print a message report-
ing how many times the loop had to run to give you a winning ticket.'''

from random import choice

my_list = ['A', 'Y', '0', 'E', '1', 'T', '2', 'Z', '3', '4',
           '5', '6', '7', '8', '9']
winning_ticket = []

copy_list = my_list.copy()    

for count in range(4):
    # Randomly choose four items and move them from the original list to the winning ticket
    item = choice(my_list)
    my_list.remove(item)
    winning_ticket.append(item)
    count +=1

my_ticket = []
time_to_win = 0
while my_ticket != winning_ticket:
    # How many tries will it take to pull a winning ticket
    my_ticket = []
    for count in range(4):
        # Randomly choose four items and move them from the copy list to my ticket
        item = choice(copy_list)
        my_ticket.append(item)
        count +=1
    time_to_win += 1

print(f"It took {time_to_win} tries to select the winning ticket. Wow!")