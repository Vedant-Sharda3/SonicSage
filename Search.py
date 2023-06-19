from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from urllib.parse import parse_qs, urlparse

# Set up the Google API client using your API key and credentials
API_KEY = 'your_api_key'
CREDENTIALS_FILE = 'path/to/your/credentials.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
youtube = build('youtube', 'v3', credentials=credentials)

def search_video_url_by_title(title, max_results=5):
    try:
        request = youtube.search().list(
            part='snippet',
            q=title,
            type='video',
            maxResults=max_results
        )
        response = request.execute()
        video_id = response['items'][0]['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        return video_url
    except HttpError as e:
        print('An error occurred:', e)
        return None

# Example usage
video_title = 'your_video_title'
video_url = search_video_url_by_title(video_title)
print(f"The URL of the video '{video_title}' is: {video_url}")