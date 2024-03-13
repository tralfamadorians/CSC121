'''8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print a
sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.'''

def make_shirt(size, text):
    # Prints tshirt size and message
    print(f"Your shirt is a size {size.lower()} and your message is: \n {text}")

make_shirt("small", "This is a good shirt.")

make_shirt(text = "This is a good shirt.", size = "small")