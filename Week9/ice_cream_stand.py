'''9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote in
Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
will work; just pick the one you like better. Add an attribute called flavors that
stores a list of ice cream flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method.'''

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # Store information on restaurants
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 770
    
    def describe_restaurant(self):
        # Print information about restaurant
        print(f"Name: {self.restaurant_name}")
        print(f"Type of Cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        # Announce that restaurant is open
        print(f"The {self.restaurant_name.title()} restaurant is open!")

    def set_number_served(self, served):
        # Return number of customers served
        self.number_served = served
        return self.number_served
    
    def increment_number_served(self, increment_served):
        # Return updated incremented number of customers served
        self.number_served += increment_served
        return self.number_served
    
class IceCreamStand(Restaurant):
    # Establish new ice cream stand class
    def __init__(self, restaurant_name, cuisine_type):
        # Inherit from parent Restaurant class
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Chocolate', 'Vanilla', 'Coffee']

    def flavor_display(self):
        # Print list of available flavors
        for flavor in self.flavors:
            print(flavor)

my_stand = IceCreamStand("Kelly's Ice Cream", 'Ice Cream')
my_stand.flavor_display()
                         
