'''10-4. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.'''

from pathlib import Path

# Prompt user for name and store in guest.txt file
path = Path('Week10\guest.txt')
path.write_text(input("What's your name? "))