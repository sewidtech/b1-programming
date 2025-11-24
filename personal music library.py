songs = []
genre_count = {}

print("Welcome to your music library!")

for i in range(1, 6):
    print(f"\nEnter details for song {i}:")
    song_name = input("Song Name: ").strip()
    genre = input("Genre: ").strip().lower()

    song_tuple = (song_name, genre)
    songs.append(song_tuple)

    genre_count[genre] = genre_count.get(genre, 0) + 1


# display library
print("\n=== YOUR MUSIC LIBRARY ===")
for idx, (name, genre) in enumerate(songs, 1):
    print(f"{idx}. {name} - Genre: {genre.capitalize()}")


# Display stats
print("\n=== GENRE STATISTICS ===")
for genre, count in genre_count.items():
    print(f"{genre}: {count} songs")


# Most popular genre
most_popular_genre = max(genre_count, key=genre_count.get)
print(f"\nMost popular genre: {most_popular_genre}")
