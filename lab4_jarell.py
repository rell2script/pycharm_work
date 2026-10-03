print ("playlist".title())
songs = ["Blinding Lights", "As It Was", "Levitating", "Flowers", "Perfect",
         "Anti-Hero", "Shape of You", "Believer", "Cruel Summer", "Counting Stars"]
lengths = [3.20, 3.47, 3.23, 4.23, 4.39, 4.21, 3.35, 3.50, 3.57, 3.05]

# 1. Show information about the original playlist
print("Number of songs:", len(songs))
print("First song:", songs[0])
print("Last song:", songs[-1])
print("Opening songs:", songs[:3])
print("Closing songs:", songs[-3:])

# 2. Every other song, starting with the first
short_playlist = songs[::3]
print("Short playlist:", short_playlist)

# 3. Add songs to the end
songs.extend(["Watermelon Sugar", "Save Your Tears"])

# 4. Remove songs
songs.remove("Perfect")
songs.remove("Believer")

# 5. Copy and sort
alphabetical_songs = sorted(songs)
print("Updated playlist:", songs)
print("Alphabetical playlist:", alphabetical_songs)

# 6. find song lengths
total_length = sum(lengths)
shortest_song = min(lengths)
longest_song = max(lengths)
average_length = total_length / len(lengths)

print(f"Total playlist length: {total_length:.2f} minutes")
print(f"Shortest song: {shortest_song:.2f} minutes")
print(f"Longest song: {longest_song:.2f} minutes")
print(f"Average song length: {average_length:.2f} minutes")

# 7. First two and last two songs in the updated playlist
playlist_preview = songs[:2] + songs[-2:]
print("Playlist preview:", playlist_preview)
