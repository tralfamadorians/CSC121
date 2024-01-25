"""Add a print() call to the end of your program informing people that you found a bigger dinner table.
Use insert() to add one new guest to the beginning of your list.
Use insert() to add one new guest to the middle of your list.
Use append() to add one new guest to the end of your list.
Use sort() to change your list so it’s stored in alphabetical order (A-Z).
Print a new set of sorted invitation messages, one for each person in your list."""

dinnerGuests = ['Antonio', 'Karen', 'Ken']

print(f"Dinner's at 8, {dinnerGuests[0]}!")
print(f"Would you like to join us, {dinnerGuests[1]}?")
print(f"If you're finished with work, I hope you can come to dinner too, {dinnerGuests[2]}!")
print("We found a bigger table!")

dinnerGuests.insert(0, 'Dad')
dinnerGuests.insert(2, 'Marianne')
dinnerGuests.append('Emma')
dinnerGuests.sort()

print(f"I hope to see you at 8 at our new bigger gathering, {dinnerGuests[0]}!")
print(f"I hope to see you at 8 at our new bigger gathering, {dinnerGuests[1]}!")
print(f"I hope to see you at 8 at our new bigger gathering, {dinnerGuests[2]}!")
print(f"I hope to see you at 8 at our new bigger gathering, {dinnerGuests[3]}!")
print(f"I hope to see you at 8 at our new bigger gathering, {dinnerGuests[4]}!")
print(f"I hope to see you at 8 at our new bigger gathering, {dinnerGuests[5]}!")