from pytube import YouTube
import moviepy.editor as mp
import os

video_url = "https://www.youtube.com/watch?v=xtoHuHgS9_o&pp=ygUKZGFyayBob3JzZQ%3D%3D"
yt = YouTube(video_url)
title = yt.title
print(title)
streams = yt.streams.filter(only_audio=True)
stream = streams[-1]  # Choose the first stream

temp_filename = stream.download()  # Download the video
mp_audio = mp.AudioFileClip(temp_filename)
mp_audio.write_audiofile(f"{title}.mp3")

os.remove(temp_filename)