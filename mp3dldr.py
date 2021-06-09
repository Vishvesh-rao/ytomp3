#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import sys
import time
import os
from pytube import YouTube



def mp3downloader(fname,vid_id):
    filename, video_id = fname,vid_id
        

    # creating YouTube object
    yt = YouTube("https://www.youtube.com/watch?v={id}".format(id = vid_id)) 

    # accessing audio streams of YouTube obj.(first one, more available)
    stream = yt.streams.filter(only_audio=True).first()
    # downloading a video would be: stream = yt.streams.first() 

    # download into working directory
    stream.download()

    # os.system("cp {fname}.mp4 {fname}.mp3".format(fname=filename,fname=filename))

    try:

        with open('{filename}.mp4'.format(filename = filename), 'rb') as audio:
            payload = {
                'chat_id': 972187028,
                'title': '{filename}.mp3'.format(filename=filename),
                'parse_mode': 'HTML'
            }
            files = {
                'audio': audio.read(),
            }
    
            resp = requests.post("https://api.telegram.org/bot{token}/sendAudio".format(token=''),
                                data=payload,
                                files=files).json()


        return "sucesfully converted!!"


    except:
        print("\nSorry, we tried but someone added water with diesel."+
                                       " You can try again.")

        return "OOPS failed to convert!!!"

