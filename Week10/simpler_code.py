'''10-3. Simpler Code: The program file_reader.py in this section uses a temporary
variable, lines, to show how splitlines() works. You can skip the temporary
variable and loop directly over the list that splitlines() returns:
for line in contents.splitlines():
Remove the temporary variable from each of the programs in this section,
to make them more concise.'''

from pathlib import Path

path = Path('Week10\pi_million_digits.txt')
contents = path.read_text()
pi_string = ''

for line in contents.splitlines():
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
