from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import os

TELE_TOKEN = "5288943034:AAHBRibBA1QMFccauDwF0xkhdTDDYYMH7AI"
BOT_USER_NAME = "MadeByAshish1_bot"
HEROKU_URL = "https://telegram-demo-bot-ashish.herokuapp.com/"
PORT = int(os.environ.get('PORT','8443'))