from random import choice

my_list = ['A', 'Y', '0', 'E', '1', 'T', '2', 'Z', '3', '4',
           '5', '6', '7', '8', '9']
random_list = []

count = 0
while count < 4:
    # Randomly choose four numbers and move them from the original list to the new one
    item = choice(my_list)
    if item.isdigit():
        my_list.remove(item)
        random_list.append(item)
        count +=1

while True:
    # Randomly chooses one letter and moves it from the original list to the new one
    item = choice(my_list)
    if item.isdigit() is False:
        my_list.remove(item)
        random_list.append(item)
        break

guess = input(f"Please type in your selected four numbers and one letter: ")
guess_list = [char for char in guess]

random_list_copy = random_list.copy()   # Copy to iterate over
guess_list_copy = guess_list.copy()     # Copy to iterate over

for guesses in guess_list_copy:
    # Check for matching numbers and letter and remove them if a matching pair is found
    for win in random_list_copy:
        if guesses == win:
            guess_list.remove(guesses)
            random_list.remove(win)
 
if not guess_list:  # If all were removed, then the guess_list was a win
    print("You won! Congratulations!")
else:
    print("Unfortunately, you didn't win this time.")
    
