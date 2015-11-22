from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import yaml

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.

with open('config.yml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

DEVELOPER_KEY = cfg['youtube_api_key']
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(query):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=query,
    type="video",
    part="id,snippet",
    maxResults=25
  ).execute()

  videos = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
        return "https://youtube.com/watch?v=" + search_result["id"]["videoId"]

def search(query):
  try:
    return youtube_search(query)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
