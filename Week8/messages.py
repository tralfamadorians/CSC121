'''8-9. Messages: Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.'''

messages = ['hi!', 'hello!', 'hey!']

def show_messages(messages):
    for message in messages:
        print(message)

show_messages(messages)