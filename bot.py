import logging
from uuid import uuid4
from yt_search import youtubeSearch
from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
from telegram.utils.helpers import escape_markdown
from mp3dldr import mp3downloader
import requests
from timeloop import Timeloop
from datetime import *




tl = Timeloop()


def start(update, context):
    update.message.reply_text('Hello!')


def inlinequery(update, context):
    """Handle the inline query."""
    query = update.inline_query.query

    if not query:
        videos = [
            InlineQueryResultArticle(
                id=uuid4(),
                title="Caps",
                input_message_content=InputTextMessageContent(
                    query.upper())),
            InlineQueryResultArticle(
                id=uuid4(),
                title="Bold",
                input_message_content=InputTextMessageContent(
                    "*{}*".format(escape_markdown(query)),
                    parse_mode=ParseMode.MARKDOWN)),
            InlineQueryResultArticle(
                id=uuid4(),
                title="Italic",
                input_message_content=InputTextMessageContent(
                    "_{}_".format(escape_markdown(query)),
                    parse_mode=ParseMode.MARKDOWN))]
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
                        str(result["snippet"]["title"])
                        
                    )
                )
            )
            
    print(len(videos))

    update.inline_query.answer(videos)
    

@tl.job(interval=timedelta(seconds=4))                  #------------ Checks current time to send update alerts at specified hour
def Check_Time_every_4s():
    try:
        resp = requests.post("https://api.telegram.org/bot1560738081:AAHqhhboT5oTCCO6uHhjbu8eIk42vxkqK0U/getUpdates")
        print(resp.json()['result'][-1]['message']['text'])
    except:
        print("blah")  

def main():


    updater = Updater("1560738081:AAHqhhboT5oTCCO6uHhjbu8eIk42vxkqK0U", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(InlineQueryHandler(inlinequery))

    updater.start_polling()

    tl.start(block=True)

    updater.idle()




if __name__ == '__main__':
    main()
