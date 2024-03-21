'''9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.'''

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # Store information on restaurants
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        # Print information about restaurant
        print(f"Name: {self.restaurant_name}")
        print(f"Type of Cuisine: {self.cuisine_type}\n")

    def open_restaurant(self):
        # Announce that restaurant is open
        print(f"The {self.restaurant_name.title()} restaurant is open!")

thai = Restaurant('Bangkok Garden', 'Thai')
pizza = Restaurant("Brothers' Pizza", 'Pizza')
burger = Restaurant('Five Guys', 'Burgers')


thai.describe_restaurant()
pizza.describe_restaurant()
burger.describe_restaurant()