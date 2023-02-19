from flask import Flask, request
import telegram.ext as tp
from telegram.ext import *
import os
import telegram
import requests
import json
from googletrans import Translator

TOKEN = os.getenv("BOT_TOKEN")
URL = os.getenv("URL")
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

updater = tp.Updater(TOKEN,use_context=True)
disp = updater.dispatcher
user_id = []
chat_id = 669277306
chat_id2 = []
chat_id_check=[]# list of chats to which it sends the msg
group_name = []
admins = ["yeetermeister"]
nfsb=0

@app.route("/{}".format(TOKEN), methods=["POST"])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode("utf-8").decode()

    # the first time you chat with the bot AKA the welcoming message
    if text == "/start":
        # print the welcoming message
        bot_welcome = "Hi! I respond by echoing messages. Give it a try!"
        # send the welcoming message
        bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)

    else:
        bot.sendMessage(chat_id=chat_id, text=text)

    return "ok"


@app.route("/setwebhook", methods=["GET", "POST"])
def set_webhook():
    # we use the bot object to link the bot to our app which live
    # in the link provided by URL
    s = bot.setWebhook("{URL}{HOOK}".format(URL=URL, HOOK=TOKEN))
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route("/")
def index():
    return "Hello, welcome to the telegram bot index page"


if __name__ == "__main__":
    # note the threaded arg which allow
    # your app to have more than one thread
    app.run(threaded=True)

