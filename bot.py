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



# # Enable logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)

# logger = logging.getLogger(__name__)


tl = Timeloop()

#Command handlers
#Sends message when /start is used
def start(update, context):
    update.message.reply_text('Hello!')

#Sends message when /search is used
def help(update, context):
    update.message.reply_text('Help!')

#Sends message when @botname is used
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
    




# def error(update, context):
#     """Log Errors caused by Updates."""
#     logger.warning('Update "%s" caused error "%s"', update, context.error)



@tl.job(interval=timedelta(seconds=4))                  #------------ Checks current time to send update alerts at specified hour
def Check_Time_every_4s():
    try:
        resp = requests.post("https://api.telegram.org/bot1560738081:AAHqhhboT5oTCCO6uHhjbu8eIk42vxkqK0U/getUpdates")
        print(resp.json()['result'][-1]['message']['text'])
    except:
        print("blah")  

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks


    updater = Updater("1560738081:AAHqhhboT5oTCCO6uHhjbu8eIk42vxkqK0U", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(InlineQueryHandler(inlinequery))

    updater.start_polling()

    tl.start(block=True)

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


    # # log all errors
    # dp.add_error_handler(error)

    # Start the Bot


if __name__ == '__main__':
    main()
