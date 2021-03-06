from turtle import update
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import os

TELE_TOKEN = "5264455127:AAHjR7B5ETqcC27iIsUhHMeYBQnffS-xogQ"
BOT_USER_NAME = "ChipTradingBot"
HEROKU_URL = "https://chip-trading-bot.herokuapp.com/"
PORT = int(os.environ.get('PORT','8443'))
  
watchlist = []
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hii, How are you doing? We are here to help you keep updated on your favourite stocks")
    update.message.reply_text("🥳")
    update.message.reply_text("/help for list of commands")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
    /add_stock - Add a stock to your watchlist
    /motivate_me - get motivational quotes
    /how_do_i_look - get comments about yourself
    """)

"""
LIST OF COMMANDS
1. Add to watchlist
2. SET LIMIT ORDER UPDATE
3. Alerts to TRACK ORDER (every minute)
4. Change alert timings
"""

def add_stock():
    update.message.reply_text("What stock do you want to add to your watchlist?")
    watchlist.append(update.message.text)
    update.message.reply_text("Stock added to watchlist")
    update.message.reply_text("/watchlist to see your watchlist")

def watchlist():
    update.message.reply_text("Your watchlist is :-")
    update.message.reply_text(watchlist)

def userText(update: Update, context: CallbackContext):
    update.message.reply_text("What {}? Do you work bitch.".format(update.message.text))

def motivate_me(update: Update, context: CallbackContext):
	update.message.reply_text("Do it, or I will shove it up on your ass")

def how_do_look(update: Update, context: CallbackContext):
	update.message.reply_text("Ugly piece of shit, you will never get a girlfriend")


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)


#updater.dispatcher.add_handler(MessageHandler(
	# Filters out unknown commands
#	Filters.command, unknown))

# Filters out unknown messages.


def main():
    updater = Updater(TELE_TOKEN, use_context=True)
    #getting the dispatchers to register handlers
    dp = updater.dispatcher
    
    #registering commands
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('motivate_me', motivate_me))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('how_do_i_look', how_do_look))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, userText))
    #registering Message Handler to reply to user messages
    #dp.add_handler(MessageHandler(Filters.text & ~Filters.command,userText))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, userText))

    #starting the bot
    updater.start_webhook(listen = "0.0.0.0", port = int(PORT), url_path = TELE_TOKEN,
                        webhook_url = HEROKU_URL+TELE_TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()