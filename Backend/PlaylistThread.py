import pandas as pd
import pygame
import time
import threading
from Backend.Playlist import createCSV




def threaded_player(songs):
    for song in songs:
        print(song)
        # play_song(song)
        pygame.mixer.init()
        length = pygame.mixer.Sound(f'C:/Users/vedant.sharda/PycharmProjects/SonicSage/Backend/songs_mp3/{song}.mp3').get_length()
        print(length)
        pygame.mixer.music.load(f'C:/Users/vedant.sharda/PycharmProjects/SonicSage/Backend/songs_mp3/{song}.mp3')
        pygame.mixer.music.set_endevent(1)
        pygame.mixer.music.play()

        while True:
            time.sleep(1)
            if (pygame.mixer.music.get_pos()/1000 + 4) > length or pygame.mixer.music.get_pos() < 0:
                pygame.mixer.music.fadeout(4)
                print(3)
                break


def playlist_player():
    createCSV()
    data = pd.read_csv('C:/Users/vedant.sharda/PycharmProjects/SonicSage/Backend/song_names.csv')
    song_names = list(data.Song)
    t1 = threading.Thread(target=threaded_player, args=[song_names])
    t1.start()
    return

