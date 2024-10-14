# class Song:
#     pass

class Song:
    # Class attributes
    count = 0  # To keep track of the number of songs
    genres = []  # List to store unique genres
    artists = []  # List to store unique artists
    genre_count = {}  # Dictionary to count songs by genre
    artist_count = {}  # Dictionary to count songs by artist

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the song count
        Song.add_song_to_count()

        # Add genre and artist to their respective lists and counts
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Example usage
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
print(ninety_nine_problems.name)  # Output: "99 Problems"
print(ninety_nine_problems.artist)  # Output: "Jay-Z"
print(ninety_nine_problems.genre)  # Output: "Rap"

# Create more songs
another_song = Song("Hotline Bling", "Drake", "Rap")
yet_another_song = Song("Halo", "Beyonce", "Pop")
print(Song.count)  # Output: 3
print(Song.artists)  # Output: ["Jay-Z", "Drake", "Beyonce"]
print(Song.genres)  # Output: ["Rap", "Pop"]
print(Song.genre_count)  # Output: {"Rap": 2, "Pop": 1}
print(Song.artist_count)  # Output: {"Jay-Z": 1, "Drake": 1, "Beyonce": 1}
