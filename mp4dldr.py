#!/usr/bin/python3
from pytube import YouTube
import requests
import sys
import os

def mp4downloader(fname,vid_id):
    filename, video_id = fname,vid_id
    
    # creating YouTube object
    yt = YouTube("https://www.youtube.com/watch?v={id}".format(id = vid_id)) 
    stream = yt.streams.first()
    stream.download()

    os.system("cp *.mp4 file.mp4")

    try:

        with open('file.mp4', 'rb') as video:
            payload = {
                'chat_id': chatid,   ## input chat id
                'title': '{filename}.mp4'.format(filename=filename),
                'parse_mode': 'HTML'
            }
            files = {
                'video': video.read(),
            }
    
            resp = requests.post("https://api.telegram.org/bot{token}/sendVideo".format(token='{bot-token}'),
                                data=payload,
                                files=files).json()

        os.system("rm *.mp4")

        return "sucesfully converted!!"


    except exception as e:
        print(e)
        os.system("rm *.mp4")

        return "OOPS failed to convert!!!"

