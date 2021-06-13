from googleapiclient.discovery import build
import requests
import json


class youtubeSearch():

    def __init__(self):
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.credentials = "API CREDS"    ## INPUT YOUR API CRED HERE
        self.message = ""
        self.description = ""
        self.results = []


    #method for starting a youtube search
    def main(self, query):

        # Get credentials and create an API client
        youtube = build(self.api_service_name, self.api_version, developerKey= self.credentials)

        request = youtube.search().list(
            part="snippet",
            maxResults=1,
            order="relevance",
            q = query,
            type="video"
        ).execute()

        # extracting the results from search response 
        self.results = request.get("items", []) 
        # empty list to store video
        videos = []
        
        # extracting required info from each result object 
        for result in self.results: 
            # video result object 
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
