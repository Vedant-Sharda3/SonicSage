import pandas as pd
import pygame
import time
import random as rd
import threading
from Backend.Playlist import createCSV
current = ''
queue = []


def threaded_player(songs):
    global current
    pygame.mixer.init()
    # global queue
    # queue = songs
    try:
        for song in songs:
            print(song)
            # play_song(song)

            current = song
            length = pygame.mixer.Sound(f'C:/Users/athar/PycharmProjects/SonicSage/Backend/songs_mp3/{song}.mp3').get_length()
            print(length)
            pygame.mixer.music.load(f'C:/Users/athar/PycharmProjects/SonicSage/Backend/songs_mp3/{song}.mp3')
            pygame.mixer.music.set_endevent(1)
            pygame.mixer.music.play()

            while True:
                time.sleep(1)
                if (pygame.mixer.music.get_pos()/1000 + 4) > length or pygame.mixer.music.get_pos() < 0:
                    pygame.mixer.music.fadeout(4)
                    print(3)
                    break
    except:
        print("Quit playlist")
        # global current
        current = ""


def playlist_player():
    createCSV()
    data = pd.read_csv('C:/Users/athar/PycharmProjects/SonicSage/Backend/song_names.csv')
    song_names = list(data.Song)
    t1 = threading.Thread(target=threaded_player, args=[song_names])
    t1.start()
    return


def playlist_player_shuffled():
    createCSV()
    data = pd.read_csv('C:/Users/athar/PycharmProjects/SonicSage/Backend/song_names.csv')
    song_names = list(data.Song)
    rd.shuffle(song_names)
    print(song_names)
    t1 = threading.Thread(target=threaded_player, args=[song_names])
    t1.start()
    return


def play_song(song):
    try:
        data = pd.read_csv('C:/Users/athar/PycharmProjects/SonicSage/Backend/song_names.csv')
        song_names = list(data.Song)
        song = song.replace('/', '').replace('|', '').replace(':', '').replace('"', '').replace('-', '')
        for i in range(len(song_names)):
            if song in song_names[i]:
                song = song_names[i]
                break
        pygame.mixer.init()
        pygame.mixer.music.load(f'C:/Users/athar/PycharmProjects/SonicSage/Backend/songs_mp3/{song}.mp3')
        global current
        current = song
        pygame.mixer.music.play()
        return 0
    except:
        print(song + " not available")
        return 1


def get_curr():
    return current
