import requests
import json
import configparser as cfg
from googleapiclient.discovery import build


class youtubeSearch():

    def __init__(self):
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.credentials = ""
        self.message = ""
        self.description = ""
        self.results = []


    def main(self, query):

        # Get credentials and create an API client
        youtube = build(self.api_service_name, self.api_version, developerKey= self.credentials)

        request = youtube.search().list(
            part="snippet",
            maxResults=10,
            order="relevance",
            q = query,
            type="video"
        ).execute()

        self.results = request.get("items", []) 
        videos = []
        
        for result in self.results: 
            info = []
            videos.append([
                result["id"]["videoId"], 
                result["snippet"]["title"], 
                result['snippet']['description'], 
                result['snippet']['thumbnails']['default']['url'],
                result['snippet']['channelTitle']])
        
        videos.append(info) 
        videoID = videos[0][0]
        _videoID = videos[0][1]
        self.message = "https://www.youtube.com/watch?v={}".format(videoID)
        self.description = _videoID
        print(_videoID)
