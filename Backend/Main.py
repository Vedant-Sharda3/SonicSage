import os
from downloader import download
from Search import search_video_url_by_title
from speech_text import convert_wav_to_text
from Audio_Recorder import record_audio
from Playlist import *


def main():
    print("What would you like to download today? Speak now...")
    # Record the Audio
    duration = 6  # Duration in seconds
    filename = "recorded_audio.wav"
    record_audio(duration, filename)
    print(f"Audio recorded for {duration} seconds and saved as {filename}")

    # Read the Instruction
    wav_file_path = "recorded_audio.wav"
    result = convert_wav_to_text(wav_file_path)
    print(result)
    os.remove('recorded_audio.wav')

    title = download(search_video_url_by_title(result))
    check = input('Would you like to play this song?')
    if check == 'yes':
        play_song(title)
    song = input('What song do you want to play?')
    play_song(song)


if __name__ == '__main__':
    main()