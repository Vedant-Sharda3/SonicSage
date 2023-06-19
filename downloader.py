from pytube import YouTube
import moviepy.editor as mp
import os


def get_links():
    print("Paste the links of your favourite songs!")
    links = []
    while True:
        link = input("Enter a link (or 'done' to finish): ")
        if link == "done" or link == 'Done':
            break
        links.append(str(link))
    return links


def download(video_url):
    yt = YouTube(video_url)
    title = yt.title
    print(title)
    streams = yt.streams.filter(only_audio=True)
    stream = streams[-1]  # Choose the first stream

    temp_filename = stream.download()  # Download the video
    mp_audio = mp.AudioFileClip(temp_filename)
    # Make sure you change the directory
    mp_audio.write_audiofile(f"{title}.mp3")

    os.remove(temp_filename)


test = get_links()
for link in test:
    download(link)
