'''9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.'''

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

class Admin(User):
    # Create special Admin type of User
    def __init__(self, first_name, last_name, city, state, age):
        # Attributes of Admin
        super().__init__(first_name, last_name, city, state, age)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        # Print list of assigned privileges
        for privilege in self.privileges:
            print(f"{privilege.title()}")

user0 = User('Kelly', 'Rivera meyers', 'Asheville', 'NC', 41)
user1 = User('Antonio', 'Rivera Martinez', 'Asheville', 'NC', 49)
user2 = Admin('walter', 'meyers', 'mathews', 'VA', 72)
user3 = User('antonio', 'rivera', 'badajoz', 'SP', 90)

user2.show_privileges()