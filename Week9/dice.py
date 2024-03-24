'''9-13. Dice: Make a class Die with one attribute called sides, which has a

default value of 6. Write a method called roll_die() that prints a random num-
ber between 1 and the number of sides the die has. Make a 6-sided die and

roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.'''

from random import randint

class Die:
    # Create the Die class

    def __init__(self, sides=6):
        # Default six sides to die
        self.sides = sides

    def roll_die(self):
        # Roll the die
        return randint(1, self.sides)
    
my_die = Die()  # Create my die

for n in range(10):
    # Roll the 6 sided die 10x
    roll = my_die.roll_die()
    print(roll)
    n += 1
print("\n")

larger_die = Die(10)    #Create 10 sided die
for n in range(10):
    # Roll the 10 sided die 10x
    roll = larger_die.roll_die()
    print(roll)
    n += 1
print("\n")

largest_die = Die(20)    #Create 20 sided die
for n in range(10):
    # Roll the 20 sided die 10x
    roll = largest_die.roll_die()
    print(roll)
    n += 1
print("\n")