"""3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in
your list."""

dinnerGuests = ['Antonio', 'Karen', 'Ken']

print(f"Dinner's at 8, {dinnerGuests[0]}!")
print(f"Would you like to join us, {dinnerGuests[1]}?")
print(f"If you're finished with work, I hope you can come to dinner too, {dinnerGuests[2]}!")

print(dinnerGuests[2])

dinnerGuests[2] = 'Dad'

print(f"I hope to see you at dinner, {dinnerGuests[0]}!")
print(f"I hope to see you at dinner, {dinnerGuests[1]}!")
print(f"I hope to see you at dinner, {dinnerGuests[2]}!")