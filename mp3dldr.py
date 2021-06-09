#!/usr/bin/python3
from pytube import YouTube
import requests
import time
import sys
import os

def mp3downloader(fname,vid_id):
    filename, video_id = fname,vid_id
        

    # creating YouTube object
    yt = YouTube("https://www.youtube.com/watch?v={id}".format(id = vid_id)) 
    stream = yt.streams.filter(only_audio=True).first()
    stream.download()

    os.system("cp *.mp4 file.mp3")
    os.system("rm *.mp4")

    try:

        with open('file.mp3', 'rb') as audio:
            payload = {
                'chat_id': "{input your chat id here}",                          ##----> input chatid
                'title': '{filename}.mp3'.format(filename=filename),
                'parse_mode': 'HTML'
            }
            files = {
                'audio': audio.read(),
            }
    
            resp = requests.post("https://api.telegram.org/bot{token}/sendAudio".format(token='bot-token'),   ##-----> input bot token
                                data=payload,
                                files=files).json()

        os.system("rm file.mp3")

        return "sucesfully converted!!"


    except exception as e:
        print(e)

        return "OOPS failed to convert!!!"

