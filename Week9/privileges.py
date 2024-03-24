'''9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.'''

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
        self.privileges = Privileges()

class Privileges:
    # Create separate Privileges class
    def __init__(self, privileges = ["can add post", "can delete post", "can ban user"]):
        # Attribute of list of privileges
        self.privileges = privileges

    def show_privileges(self):
        # Print list of assigned privileges
        for privilege in self.privileges:
            print(f"{privilege.title()}")

user1 = Admin('Antonio', 'Rivera Martinez', 'Asheville', 'NC', 49)
user1.privileges.show_privileges()