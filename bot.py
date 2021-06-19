from telegram import InlineQueryResultArticle, InlineKeyboardButton, InlineKeyboardMarkup, Update, InputTextMessageContent, Bot
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, CallbackQueryHandler, CallbackContext
from yt_search import youtubeSearch
from mp3dldr import mp3downloader
from mp4dldr import mp4downloader
from timeloop import Timeloop
from uuid import uuid4
from datetime import *
import requests
import logging

videoId = ''
SongName = ''
chatid = ''

def initVars(vId,sName):

    
    global videoId 
    global SongName 

    try:
        videoId = vId
        SongName = sName

        SendMesgg(SongName)

        # print("inintvars",videoId)
        # print("inintvars",SongName)
        return "/convert \nVideoID: {videoId} \nSong name: {SongName}".format(videoId,SongName)

    except:
        return "/convert selected song"

def start(update, context):
     update.message.reply_text('Hello!')

def help(update, context):
    update.message.reply_text('Help!')

def convert(update, context):
    
    global chatid

    keyboard = [
    
        [InlineKeyboardButton("Convert To Mp3", callback_data="mp3"),InlineKeyboardButton("Convert To Mp4", callback_data='mp4'),],

        [InlineKeyboardButton("Cancel/Retry Conversion", callback_data='cancelled')],

               ]

    print(SongName)
    print(videoId)

    reply_markup = InlineKeyboardMarkup(keyboard)

    content = "<b>Video Info</b>\n_____________________\n\n<b>VideoID-></b>   <code>" + videoId + "</code>\n\n<b>Video Name-></b>   <code>" + SongName + "</code>\n\n<i>Please choose</i>"

    update.message.reply_text(content,parse_mode='HTML',reply_markup=reply_markup)
    
    chatid = update.message.chat.id

def button(update ,context) -> None:

    query = update.callback_query
    query.answer()

    type_ = query.data

    if query.data == 'cancelled':

        query.edit_message_text("<b>Video conversion cancelled!!!</b>\n\n<b><i>Please choose again to coonvert!!</i></b>",parse_mode='HTML')

    else:

        query.edit_message_text("<b>Video Info</b>\n_____________________\n\n<b>VideoID-></b>   <code>" + videoId + "</code>\n\n<b>Video Name-></b>   <code>" + SongName + "</code>\n\n<b>Converting to-></b>   <code>" + type_ + "</code>\n\n<b><i>please wait while converting.......</i></b>",parse_mode='HTML')

        if query.data == 'mp3':
            mp3downloader(SongName,videoId,chatid)

        if query.data == 'mp4':
            mp4downloader(SongName,videoId,chatid)

        query.edit_message_text(text="<b>Video Info</b>\n_____________________ \n\n<b>VideoID-></b>   <code>" + videoId + "</code>\n\n<b>Video Name-></b>   <code>" + SongName + "</code>\n\n<b><i>Video Converted!!</i></b>",parse_mode='HTML')


#Sends message when @botname is used
def inlinequery(update, context):

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
    updater = Updater("{bot-token}", use_context=True)                  ## INPUT BOT TOKEN HERE

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("convert", convert))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(InlineQueryHandler(inlinequery))

    updater.start_polling()

 
    updater.idle()


if __name__ == '__main__':
    main()

