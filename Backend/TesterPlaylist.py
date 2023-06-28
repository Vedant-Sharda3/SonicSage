import pygame
import os

pygame.init()
pygame.mixer.init()


songs_directory = "songs_mp3"
song_files = os.listdir(songs_directory)
playlist = []
current_song_index = 0
is_playing = False

# Create playlist
for song_file in song_files:
    song_path = os.path.join(songs_directory, song_file)
    playlist.append(song_path)

# Function to play the current song
def play_song():
    global is_playing
    pygame.mixer.music.load(playlist[current_song_index])
    pygame.mixer.music.play()
    is_playing = True

# Function to pause the current song
def pause_song():
    global is_playing
    pygame.mixer.music.pause()
    is_playing = False

# Function to resume the current song
def resume_song():
    global is_playing
    pygame.mixer.music.unpause()
    is_playing = True

# Function to play the next song
def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist)
    pygame.mixer.music.stop()
    play_song()

screen = pygame.display.set_mode((400, 300))

# Play the first song
play_song()

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_playing:
                    pause_song()
                else:
                    resume_song()
            elif event.key == pygame.K_RIGHT:
                next_song()

    # Check if the current song has finished playing
    if not pygame.mixer.music.get_busy() and is_playing:
        next_song()

    # Add a small delay to reduce CPU usage
    pygame.time.delay(100)

pygame.quit()


