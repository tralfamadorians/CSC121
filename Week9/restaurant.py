'''9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of

information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.

Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.'''

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # Store information on restaurants
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        # Print information about restaurant
        print(f"Name: {self.restaurant_name}")
        print(f"Type of Cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        # Announce that restaurant is open
        print(f"The {self.restaurant_name.title()} restaurant is open!")

restaurant = Restaurant('Bangkok Garden', 'Thai')

restaurant.describe_restaurant()
restaurant.open_restaurant()