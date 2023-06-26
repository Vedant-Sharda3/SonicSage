from youtube_search import YoutubeSearch
from pytube import YouTube
#https://coolors.co/fcde9c-ffa552-ba5624-381d2a-c4d6b0

def search_video_url_by_title(title):
    results = YoutubeSearch(title + "song lyrics", max_results=1).to_dict()
    video_url = 'Error'
    if results:
        video_id = results[0]['id']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
    return video_url

def search_video_title(title):
    results = YoutubeSearch(title + "song lyrics", max_results=1).to_dict()
    title = ''
    if results:
        video_id = results[0]['id']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        yt = YouTube(video_url)
        title = yt.title
    return title

# Example usage
# video_title = "Dark horse katy perry lyrics"
# video_url = search_video_url_by_title(video_title)
# print(video_url)