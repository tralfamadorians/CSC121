'''9-5. Login Attempts: Add an attribute called login_attempts to your User class
from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.'''

class User:
    def __init__(self, first_name, last_name, city, state, age):
        # Store attributes about an user
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        # Print information about user
        print(f"First Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"City: {self.city.title()}")
        print(f"State: {self.state}")
        print(f"Age: {self.age}\n")

    def greet_user(self):
        # Print greeting to user
        print(f"Welcome {self.first_name.title()}!\n")
    
    def increment_login_attempts(self):
        # Track number of login attempts
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        # Resets login attempts to zero
        self.login_attempts = 0

user0 = User('Kelly', 'Rivera meyers', 'Asheville', 'NC', 41)
user1 = User('Antonio', 'Rivera Martinez', 'Asheville', 'NC', 49)
user2 = User('walter', 'meyers', 'mathews', 'VA', 72)
user3 = User('antonio', 'rivera', 'badajoz', 'SP', 90)

users = [user0, user1, user2, user3]

for user in users:
    user.describe_user()
    user.greet_user()

for i in range(4):
    user0.increment_login_attempts()
    i += 1
print(f"{user0.first_name.title()}'s login attempts: {user0.login_attempts}")

user0.reset_login_attempts()
print(f"{user0.first_name.title()}'s login attempts: {user0.login_attempts}")