'''9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters.
Randomly select 4 numbers or letters from the list and print a message saying that
any ticket matching these 4 numbers or letters wins a prize.'''

from random import  choice

my_list = ['A', 'Y', '0', 'E', '1', 'T', '2', 'Z', '3', '4',
           '5', '6', '7', '8', '9']
random_list = []

for count in range(4):
    # Randomly choose four items and move them from the original list to the new one
    item = choice(my_list)
    my_list.remove(item)
    random_list.append(item)
    count +=1

print(f"Any ticket matching the following four numbers or letters wins a prize!\n {random_list}")