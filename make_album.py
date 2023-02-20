def make_album(artist_name, album_title, number_songs = None):
    """function with while loop"""
    if number_songs:
        album = {'artist_name' : artist_name, 'album_title' : album_title, 'number_songs' : number_songs}
    else:
        album = {'artist_name' : artist_name, 'album_title' : album_title}
    return album

music1 = make_album('Michael Jackson', 'Thriller', 30)
music2 = make_album('Queen', 'A Night at the Opera')
music3 = make_album('Metallica', '...And Justice for All', 3)

while True:
    artistName = input("\nPlease enter the name of the artist: ")
    print("(enter 'q' at any time to quit)")

    if artistName == 'q':
        break
    
    albumTitle = input("\nPlease enter the title of the album: ")
    print("(enter 'q' at any time to quit)") 

    if albumTitle == 'q':
        break   

    songs = input("\nHow many songs does the album have?: ")
    print("(enter 'q' at any time to quit)") 

    if songs == 'q':
        break   


print(music1)
print(music2)
print(music3)
