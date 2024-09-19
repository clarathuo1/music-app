import sys
from models import add_artist, add_album, get_albums_by_artist, get_albums_by_genre, delete_album, list_artists, list_albums

def main():
    while True:
        print("Album Manager CLI")
        print("1. Add Artist")
        print("2. Add Album")
        print("3. List Artists")
        print("4. List Albums")
        print("5. Get Albums by Artist")
        print("6. Get Albums by Genre")
        print("7. Delete Album")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter artist name: ")
            add_artist(name)
            print("Artist added.")
        
        elif choice == '2':
            title = input("Enter album title: ")
            artist_name = input("Enter artist name: ")
            genre_name = input("Enter genre name: ")
            add_album(title, artist_name, genre_name)
            print("Album added.")
        
        elif choice == '3':
            artists = list_artists()
            for artist in artists:
                print(artist.name)
        
        elif choice == '4':
            albums = list_albums()
            for album in albums:
                print(f"{album.title} by {album.artist.name} ({album.genre.name})")
        
        elif choice == '5':
            artist_name = input("Enter artist name: ")
            albums = get_albums_by_artist(artist_name)
            for album in albums:
                print(album.title)
        
        elif choice == '6':
            genre_name = input("Enter genre name: ")
            albums = get_albums_by_genre(genre_name)
            for album in albums:
                print(album.title)
        
        elif choice == '7':
            album_id = int(input("Enter album ID to delete: "))
            delete_album(album_id)
            print("Album deleted.")
        
        elif choice == '8':
            print("Exiting...")
            sys.exit()
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
