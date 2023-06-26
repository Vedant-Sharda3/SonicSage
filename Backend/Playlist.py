import os
import pandas as pd
import pygame


def createCSV():
    file_names = os.listdir('songs_mp3')

    if os.path.exists('song_names.csv'):
        data = pd.read_csv('song_names.csv')
        song_names = list(data.Song)
        for name in song_names:
            name = name + '.mp3'
            if name not in file_names:
                data.drop(data[data['Song'] == name.replace('.mp3', '')].index, inplace = True)
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


def player(userInput):
    if userInput == 'p':

        # Pause the music
        pygame.mixer.music.pause()
        print("music is paused....")
        return 0
    elif userInput == 'r':

        # Resume the music
        pygame.mixer.music.unpause()
        print("music is resumed....")
        return 0
    elif userInput == 'e':

        # Stop the music playback
        pygame.mixer.music.stop()
        print("music is stopped....")
        return 1


def play_song(song):

    data = pd.read_csv('C:/Users/athar/PycharmProjects/SonicSage/Backend/song_names.csv')
    song_names = list(data.Song)
    for i in range(len(song_names)):
        print(song_names[i])
        if song in song_names[i]:
            print(song_names[i])
            song = song_names[i]
            print('name is ', song)
            break
    pygame.mixer.init()
    pygame.mixer.music.load(f'C:/Users/athar/PycharmProjects/SonicSage/Backend/songs_mp3/{song}.mp3')
    pygame.mixer.music.play()
    return
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


# createCSV()
# likeSong('Gallan')
# temp = os.listdir('songs_mp3')[3].replace('.mp3', '')
# print(temp)
# play_song(temp)
# # delete_song(temp)
# for i in ['GREECE', 'rockstar', 'Box']:
#     play_song(i)