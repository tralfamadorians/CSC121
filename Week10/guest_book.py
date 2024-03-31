from pathlib import Path
path = Path('Week10\guest_book.txt')

# Create a txt file and store guest names one per line and greet them as their name is inputted.
guest_book = ''
while True:
    new_guest = input("What's the name of the next guest? ")
    print(f"Welcome, {new_guest}!")
    guest_book += new_guest + '\n'
    if input("Are there more guests to add? (Y/N) ") == 'N':
        break

path.write_text(guest_book)