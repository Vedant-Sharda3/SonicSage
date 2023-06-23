import os
import pandas as pd
import pygame


def createCSV():
    file_names = os.listdir('songs_mp3')

    if os.path.exists('song_names.csv'):
        data = pd.read_csv('song_names.csv')
        song_names = list(data.Song)
        prev = len(song_names)
        liked = list(data.Liked)
        played = list(data.Played)
        for name in file_names:
            name = name.replace('.mp3', '')
            if name not in list(data.Song):
                song_names.append(name)
                liked.append(0)
                played.append(0)
        aft = len(song_names)
        df = pd.DataFrame({'Song': song_names,
                           'Liked': liked,
                           'Played': played
                           })
        df.to_csv('song_names.csv', index=False)
        if prev == aft:
            print('CSV already up to date!')
        else:
            print('CSV updated!')
        return

    song_names = []
    liked = []
    played = []
    for name in file_names:
        song_names.append(name.replace('.mp3', ''))
        liked.append(0)
        played.append(0)

    df = pd.DataFrame({'Song': song_names,
                       'Liked': liked,
                       'Played': played
                       })
    df.to_csv('song_names.csv', index=False)
    print('CSV created!')


def likeSong(song):
    data = pd.read_csv('song_names.csv')
    song_names = list(data.Song)
    liked = list(data.Liked)
    played = list(data.Played)
    for i in range(len(song_names)):
        if song in song_names[i]:
            if liked[i] == 0:
                liked[i] = 1
                print(f'liked {song}!')
            else:
                liked[i] = 0
                print(f'unliked {song}!')
            break
    df = pd.DataFrame({'Song': song_names,
                       'Liked': liked,
                       'Played': played
                       })
    df.to_csv('song_names.csv', index=False)
    print(f'updated CSV!')


def delete_song(song):
    path = f'songs_mp3/{song}.mp3'
    if os.path.exists(path):
        os.remove(path)
        print("File deleted successfully.")
        data = pd.read_csv('song_names.csv')
        song_names = list(data.Song)
        for i in range(len(song_names)):
            if song in song_names[i]:
                data = data.drop(index=i)
        data.to_csv('song_names.csv', index=False)
        print(f'updated CSV!')
    else:
        print("File not found.")


def play_song(song):
    pygame.mixer.init()
    pygame.mixer.music.load(f'songs_mp3/{song}.mp3')
    pygame.mixer.music.play()
    while True:
        print("------------------------------------------------------------------------------------")
        print("Press 'p' to pause the music")
        print("Press 'r' to resume the music")
        print("Press 'e' to exit the program")

        # take user input
        userInput = input("-->")

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
            pygame.mixer.music.stop()
            print("music is stopped....")
            break

