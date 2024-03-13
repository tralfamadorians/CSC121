'''8-11. Archived Messages: Start with your work from Exercise 8-10. Call the func-
tion send_messages() with a copy of the list of messages. After calling the func-
tion, print both of your lists to show that the original list has retained its messages.'''

messages = ['hi!', 'hello!', 'hey!']
sent_messages= []

def show_messages(messages):
    # Prints list of messages
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    # Messages moved from messages to sent messages and printed as they move
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)