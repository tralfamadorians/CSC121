'''10-5. Guest Book: Write a while loop that prompts users for their name. Collect
all the names that are entered, and then write these names to a file called
guest_book.txt. Make sure each entry appears on a new line in the file.'''

from pathlib import Path
path = Path('Week10\guest_book.txt')

guest_book = ''
while True:
    guest_book += input("What's the name of the next guest? ") + '\n'
    if input("Are there more guests to add? (Y/N) ") == 'N':
        break

path.write_text(guest_book)