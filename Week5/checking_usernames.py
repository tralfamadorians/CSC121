"""5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
current_users containing the lowercase versions of all existing users.)"""

current_users = ['john', 'jane', 'alice', 'bob', 'jordan']
new_users = ['john', 'jane', 'kelly', 'antonio', 'sean']

for new_user in new_users:
    duplicate = False
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            duplicate = True
    if duplicate:
        print("This username is not available. Please choose another.")
    else:
        print("This username is available.")