import pygame
import os

pygame.init()
pygame.mixer.init()

songs_directory = "songs_mp3"
song_files = os.listdir(songs_directory)
playlist = []
current_song_index = 0
is_playing = False

for song_file in song_files:
    song_path = os.path.join(songs_directory, song_file)
    playlist.append(song_path)

def play_song():
    global is_playing
    pygame.mixer.music.load(playlist[current_song_index])
    pygame.mixer.music.play()
    is_playing = True

def pause_song():
    global is_playing
    pygame.mixer.music.pause()
    is_playing = False

def resume_song():
    global is_playing
    pygame.mixer.music.unpause()
    is_playing = True

def next_song():
    global current_song_index
    if current_song_index < len(playlist) - 1:
        current_song_index += 1
    else:
        current_song_index = 0
    pygame.mixer.music.stop()
    play_song()

play_song()

screen = pygame.display.set_mode((400, 300))
running = True
while running:
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

    pygame.time.delay(100)

pygame.quit()
