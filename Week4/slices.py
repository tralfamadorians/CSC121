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

print("The first three items in the list are:")
for guest in dinnerGuests[0:3]:
    print(guest)

print("Three items from the middle of the list are:")
for guest in dinnerGuests[2:5]:
    print(guest)

print("The last three items in the list are:")
for guest in dinnerGuests[-3:]:
    print(guest)