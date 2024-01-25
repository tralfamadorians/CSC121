"""3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print a
message to that person letting them know you’re sorry you can’t invite them
to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end of
your program."""

dinnerGuests = ['Antonio', 'Karen', 'Ken']

print(f"Dinner's at 8, {dinnerGuests[0]}!")
print(f"Would you like to join us, {dinnerGuests[1]}?")
print(f"If you're finished with work, I hope you can come to dinner too, {dinnerGuests[2]}!")
print("We found a bigger table!")

dinnerGuests.insert(0, 'Dad')
dinnerGuests.insert(2, 'Marianne')
dinnerGuests.append('Miss Emma')

print(f"I hope to see you at 8 at our new bigger gathering, {dinnerGuests[0]}!")
print(f"I hope to see you at 8 at our new bigger gathering, {dinnerGuests[1]}!")
print(f"I hope to see you at 8 at our new bigger gathering, {dinnerGuests[2]}!")
print(f"I hope to see you at 8 at our new bigger gathering, {dinnerGuests[3]}!")
print(f"I hope to see you at 8 at our new bigger gathering, {dinnerGuests[4]}!")
print(f"I hope to see you at 8 at our new bigger gathering, {dinnerGuests[5]}!")

print("Sorry, the new table won't be here in time. We can only host two guests :(")

removed = dinnerGuests.pop()
print(f"Sorry, {removed} but you've been bumped from the guest list :(")
removed = dinnerGuests.pop()
print(f"Sorry, {removed} but you've been bumped from the guest list :(")
removed = dinnerGuests.pop()
print(f"Sorry, {removed} but you've been bumped from the guest list :(")
removed = dinnerGuests.pop()
print(f"Sorry, {removed} but you've been bumped from the guest list :(")

print(f"You are on the short list, {dinnerGuests[0]}!")
print(f"You are on the short list, {dinnerGuests[1]}!")

del dinnerGuests[1]
del dinnerGuests[0]

print(dinnerGuests)
