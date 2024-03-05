'''8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.'''


def make_album(name, album, songs = None):
    artist = {'Name' : name, 'Album' : album}
    if songs:
        artist['Number of Songs'] = songs
    return artist

print(make_album('R.E.M.', 'Automatic for the People'))

print(make_album('Nirvana', 'In Utero'))

print(make_album('Nine Inch Nails', 'The Downward Spiral'))

print(make_album('Nine Inch Nails', 'The Downward Spiral', 14))