class User:
    def __init__(self, first_name, last_name, city, state, age):
        # Store attributes about an user
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state
        self.age = age
    
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

user0 = User('Kelly', 'Rivera meyers', 'Asheville', 'NC', 41)
user1 = User('Antonio', 'Rivera Martinez', 'Asheville', 'NC', 49)
user2 = User('walter', 'meyers', 'mathews', 'VA', 72)
user3 = User('antonio', 'rivera', 'badajoz', 'SP', 90)

users = [user0, user1, user2, user3]

for user in users:
    user.describe_user()
    user.greet_user()

