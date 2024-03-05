'''8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.'''

def make_album(name, album, songs = None):
    artist = {'Name' : name, 'Album' : album}
    if songs:
        artist['Number of Songs'] = songs
    return artist

print(make_album('R.E.M.', 'Automatic for the People'))

print(make_album('Nirvana', 'In Utero'))

print(make_album('Nine Inch Nails', 'The Downward Spiral'))

print(make_album('Nine Inch Nails', 'The Downward Spiral', 14))