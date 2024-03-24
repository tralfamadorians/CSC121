import user_class_module

class Admin(user_class_module.User):
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