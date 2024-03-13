"""8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call."""

def favorite_book(title):
    # Prints the name of book in title format
    print(f"One of my favorite books is {title.title()}.")

favorite_book("slaughterhouse five")
