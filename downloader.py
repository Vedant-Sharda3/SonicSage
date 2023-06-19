from pytube import YouTube
import pytube
import moviepy.editor as mp
import os
from Search import search_video_url_by_title
from Playlist import createCSV


def get_links():
    print("Paste the links of your favourite songs!")
    links = []
    while True:
        link = input("Enter a link (or 'done' to finish): ")
        if link.capitalize() == "DONE":
            break
        links.append(link)
    return links


def download(video_url):
    try:
        yt = YouTube(video_url)
        title = yt.title
        print(title)
        streams = yt.streams.filter(only_audio=True)
        stream = streams[-1]  # Choose the first stream

        temp_filename = stream.download()  # Download the video
        mp_audio = mp.AudioFileClip(temp_filename)
        title = title.replace('/', '').replace('|', '').replace(':', '')
        mp_audio.write_audiofile(f"songs_mp3/{title}.mp3")

        os.remove(temp_filename)
        createCSV()
    except pytube.exceptions.VideoUnavailable as e:
        print('Invalid link!', e)
    except:
        print('Error in downloading: ' + video_url)
    return title

# links = ['https://www.youtube.com/watch?v=_HZM0QiuUS8&pp=ygUhaXJpcyAobGl2ZSkgYnkgdGhlIGdvbyBnb28gZG9sbHMg', 'https://www.youtube.com/watch?v=xtoHuHgS9_o&pp=ygUKZGFyayBob3JzZQ%3D%3D'] #get_links()
# for link in links:
#     download(link)


