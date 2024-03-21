'''9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and print
the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a day of
business.'''

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

restaurant = Restaurant('Bangkok Garden', 'Thai')

restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"Number served start of Day 4: {restaurant.set_number_served(888)}")
print(f"Number served end of Day 4: {restaurant.increment_number_served(234)}")