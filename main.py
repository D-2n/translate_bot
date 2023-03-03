import telebot as tb
from telegram.ext import *
import requests
import json
from googletrans import Translator
import time
TOKEN = '5259610624:AAGMNZmwTmX00LGno0Ykn8MiZMnVL4UK1zw'
bot=tb.TeleBot(TOKEN)
# -----------------------------------------------------
TOKEN = '5259610624:AAGMNZmwTmX00LGno0Ykn8MiZMnVL4UK1zw'
user_id = ["yeetermeister"]
chat_id = 669277306
fam = (-689737739,"sr")
chat_id2 = []
chat_id_check=[]# list of chats to which it sends the msg
group_name = []
admins = ["yeetermeister"]
nfsb=0
# -----------------------------------------------------
bot=tb.TeleBot(TOKEN)

#----------------------------------------------------------------------
def translate(text,lang):
    strale=Translator()
    prevod=strale.translate(text,dest=lang)
    return prevod.text
#----------------------------------------------------------------------
def send_fdb(bot_token,id,text):
    url = "https://api.telegram.org/bot{}/sendMessage".format(bot_token)
    params = {
        "chat_id": id,
        "text": text
    }
    response = requests.post(url, params=params)
def send_message(bot_token, chat_id2, text):
    url = "https://api.telegram.org/bot{}/sendMessage".format(bot_token)
    for chat_id in chat_id2:
        newtxt = translate("TRANSLATED AUTOMATICALLY!\n" + text, chat_id[1])
        params = {
            "chat_id": chat_id[0],
            "text": newtxt
        }
        response = requests.post(url, params=params)
def send_pv(bot_token,to_chat,pv,txt):
    url = "https://api.telegram.org/bot{}/sendPhoto".format(bot_token)
    for chat_id in to_chat:
        newtxt = translate("TRANSLATED AUTOMATICALLY!\n" + txt, chat_id[1])
        params = {
            "chat_id": chat_id[0],
            "photo": str(pv),
            "caption" : newtxt
        }
        response = requests.post(url, params=params)
#listen_for_user(bot_token, chat_id, user_id, chat_id2, nfsb)
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"Peki")
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset=-1"
lastid = None
bot_token=TOKEN
while True:
    bot.polling()

