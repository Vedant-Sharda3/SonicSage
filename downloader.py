from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=xtoHuHgS9_o&pp=ygUKZGFyayBob3JzZQ%3D%3D"
yt = YouTube(video_url)

streams = yt.streams
stream = streams[0]  # Choose the first stream

stream.download()  # Download the video