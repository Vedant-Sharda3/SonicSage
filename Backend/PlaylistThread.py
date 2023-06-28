import pandas as pd
import pygame
import time
from Playlist import play_song, player
import threading

data = pd.read_csv('C:/Users/athar/PycharmProjects/SonicSage/Backend/song_names.csv')
song_names = list(data.Song)
pygame.mixer.init()

def threaded_player(songs):
    for song in songs:
        print(song)
        # play_song(song)
        pygame.mixer.music.load(f'C:/Users/athar/PycharmProjects/SonicSage/Backend/songs_mp3/{song}.mp3')
        pygame.mixer.music.play()
        time.sleep(1)
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


t1 = threading.Thread(target=threaded_player, args=[song_names])
t1.start()

while t1.is_alive():
    userInput = input('\nEnter: ')
    if userInput == 'p':

        # Pause the music
        pygame.mixer.music.pause()
        print("music is paused....")
    elif userInput == 'r':

        # Resume the music
        pygame.mixer.music.unpause()
        print("music is resumed....")
    elif userInput == 'e':

        # Stop the music playback
        pygame.mixer.music.fadeout(4)
        print("music is stopped....")

