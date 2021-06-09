from telegram import InlineQueryResultArticle, InlineKeyboardButton, InlineKeyboardMarkup, Update, InputTextMessageContent, Bot
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, CallbackQueryHandler, CallbackContext
from yt_search import youtubeSearch
from mp3dldr import mp3downloader
from timeloop import Timeloop
from uuid import uuid4
from datetime import *
import requests
import logging

videoId = ''
SongName = ''

#Command handlers
#Sends message when /start is used
# def start(update, context):
#     update.message.reply_text('Hello!')

#Sends message when /help is used

def initVars(vId,sName):
    
    global videoId 
    global SongName 

    try:
        videoId = vId
        SongName = sName
       
        return "/convert \nVideoID: {videoId} \nSong name: {SongName}".format(videoId,SongName)

    except:
        return "/convert selected song"


def help(update, context):
    update.message.reply_text('Help!')

def convert(update, context):

    keyboard = [
    
        [InlineKeyboardButton("Convert To Mp3", callback_data='converted')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Click to convert",reply_markup=reply_markup)

def button(update ,context) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    query.answer()

    print(SongName)
    print(videoId)

    mp3downloader(SongName,videoId)

    query.edit_message_text(text=f"{query.data}")


#Sends message when @botname is used
def inlinequery(update, context):
    """Handle the inline query."""
    query = update.inline_query.query

    if not query:
        print("not query")
    else:
        _youtubesearch = youtubeSearch()
        _youtubesearch.main(query) 
        results =  _youtubesearch.results

        videos = []
        
        for result in results: 

            url = "https://www.youtube.com/watch?v={}".format(result["id"]["videoId"])
                        
            videos.append(
                InlineQueryResultArticle(
                    id = uuid4(),
                    title = result["snippet"]["title"],
                    thumb_url = result['snippet']['thumbnails']['default']['url'],
                    input_message_content = InputTextMessageContent(
                        str(initVars(result["id"]["videoId"],result["snippet"]["title"]))
                        
                    )
                )
            )
            
    print(len(videos))

    update.inline_query.answer(videos)

def main():

    print("start")
    updater = Updater("{bot-token}", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("convert", convert))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(InlineQueryHandler(inlinequery))

    updater.start_polling()

 
    updater.idle()


    # # log all errors
    # dp.add_error_handler(error)

    # Start the Bot

# def error(update, context):
#     """Log Errors caused by Updates."""
#     logger.warning('Update "%s" caused error "%s"', update, context.error)



# @tl.job(interval=timedelta(seconds=4))                  #------------ Checks current time to send update alerts at specified hour
# def Check_Time_every_4s():
#     try:
#         resp = requests.post("https://api.telegram.org/bot1560738081:AAHqhhboT5oTCCO6uHhjbu8eIk42vxkqK0U/getUpdates")
#         print(resp.json()['result'][-1]['message']['text'])
#     except:
#         print("blah")  


if __name__ == '__main__':
    main()
