# ytomp3 :musical_note:

Simple video search bot for telegram that lets the user search for videos on youtube via inline command. Now you can take full advantage of telegrams unlimited free storage and built in mp3 player without having to worry about backing up your songs or loosing them!! Now with added support for mp4 format too !!

## Requirements [_self hosting_]
```css
1. Inline telegram bot 
2. Bot Tokem from botfather
3. Youtube V3 API creds
```

## Steps for self hosting
- Clone the repo
- Run ```pip install -r requirements.txt```
- Create an inline bot using botfather ( look [here](https://core.telegram.org/bots/inline) if unsure on the steps )
- You will get a bot-token paste that in ***bot.py*** and ***mp3dldr.py*** and ***mp4dldr.py***
- you will need to get your API keys for youtube from [here](https://developers.google.com/docs/api/quickstart/python) 
- Put the API creds in ***yt_search.py***
- Run bot.py `python3 bot.py`

## Usage

- type `@botusername` in message field and type the video name (_might take a few sec for video to appear_ )
- Wait till the video appears and click on it
- press the `convert to mp3`/`convert to mp4` button which appears after that
- Wait for it to convert
- video will be downloaded


> PS: This bot is made purely for educational purposes and getting an understanding of the bot api. Certain songs are not meant to be downloaded do check TOS of youtube. 


