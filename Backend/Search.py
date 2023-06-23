from youtube_search import YoutubeSearch
import pytube

def search_video_url_by_title(title):
    results = YoutubeSearch(title, max_results=1).to_dict()
    video_url = 'Error'
    if results:
        video_id = results[0]['id']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
    return video_url
