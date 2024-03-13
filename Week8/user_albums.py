'''8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.'''

def make_album(name, album, songs = None):
    # Make album dictionary with name, album and song count, if available 
    artist = {'Name' : name, 'Album' : album}
    if songs:
        artist['Number of Songs'] = songs
    return artist

while True:
    print("Type 'q' to quit.")
    
    name = input("What's the artist's name? ")
    if name == 'q':
        break

    album = input("What's the title of the album? ")
    if album == 'q':
        break

    print(make_album(name, album))