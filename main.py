import telegram.ext as tp
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
updater = tp.Updater(TOKEN,use_context=True)
disp = updater.dispatcher
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
bot.polling()
while True:
     response = requests.get(url)
     updates = json.loads(response.text)
     upd = updates["result"][-1]
     if "message" in upd:
         if upd["update_id"] != lastid:
             lastid = upd["update_id"]
             if upd["message"]["chat"]["type"] == 'private':
                 korisnik = upd["message"]["from"]["username"]
                 if korisnik in admins:
                     if nfsb == 0:
                         nfsb = 1
                     else:
                         first = upd["message"]["text"].split(' ')[0]
                         # ADD ADMIN-----------------------------------
                         if first == "/add_admin":
                             id = upd["message"]["chat"]["id"]
                             second = upd["message"]["text"].split(' ')[1]
                             if second in admins:
                                 send_fdb(bot_token, id, "Already there!")
                             else:
                                 admins.append(second)
                                 send_fdb(bot_token, id, "Admin added!")
                         # REMOVE ADMIN -------------------------------
                         if first == "/remove_admin":
                             id = upd["message"]["chat"]["id"]
                             second = upd["message"]["text"].split(' ')[1]
                             if second in admins:
                                 admins.remove(second)
                                 send_fdb(bot_token, id, "Admin removed!")
                             else:
                                 send_fdb(bot_token, id, "Wasn't admin!")
                         # ADD SOURCE --------------------------------------
                         if first == '/add_source':
                             id = upd["message"]["chat"]["id"]
                             title = upd["message"]["text"].split(' ')[1]
                             if title in group_name:
                                 send_fdb(bot_token, id, "Source already added!")
                             else:
                                 group_name.append(title)
                                 send_fdb(bot_token, id, "Source added!")
                         # REMOVE SOURCE-------------------------------------
                         if first == '/remove_source':
                             id = upd["message"]["chat"]["id"]
                             title = upd["message"]["text"].split(' ')[1]
                             if title in group_name:
                                 group_name.remove(title)
                                 send_fdb(bot_token, id, "Source removed!")
                             else:
                                 send_fdb(bot_token, id, "Source wasn't added!")
                         # ADD LISTEN ---------------------------------------------
                         if first == '/add_listen':
                             id = upd["message"]["chat"]["id"]
                             second = upd["message"]["text"].split(' ')[1]
                             if second in user_id:
                                 send_fdb(bot_token, id, "User already added!")
                             else:
                                 user_id.append(second)
                                 send_fdb(bot_token, id, "User added!")
                         # REMOVE LISTEN--------------------------------------------------------
                         if first == '/remove_listen':
                             id = upd["message"]["chat"]["id"]
                             second = upd["message"]["text"].split(' ')[1]
                             if second in user_id:
                                 user_id.remove(second)
                                 send_fdb(bot_token, id, "User removed!")
                             else:
                                 send_fdb(bot_token, id, "User wasn't added!")
                                 print(user_id)
             tip = upd["message"]["chat"]["type"]
             if (tip in ['group', 'supergroup']):
                 korisnik = upd["message"]["from"]["username"]
                 if korisnik in user_id:
                     if nfsb == 0:
                         nfsb = 1
                     else:
                         first = upd["message"]["text"].split(' ')[0]
                         if korisnik in admins:
                             if first == '/set_out':
                                 id = upd["message"]["chat"]["id"]
                                 second = upd["message"]["text"].split(' ')[1]
                                 if id in chat_id_check:
                                     send_fdb(bot_token, id, "Chat already added to output list!")
                                 else:
                                     chat_id2.append((id, second))
                                     chat_id_check.append(id)
                                     send_fdb(bot_token, id, "Chat successfully added to output list!")
                             # REMOVE FROM OUTPUT LIST -------------------------------------------------
                             if first == '/remove_out':
                                 id = upd["message"]["chat"]["id"]
                                 if id in chat_id_check:
                                     ind = chat_id_check.index(id)
                                     chat_id_check.remove(chat_id_check[ind])
                                     chat_id2.remove(chat_id2[ind])
                                     send_fdb(bot_token, id, "Chat removed from output list!")
                                 else:
                                     send_fdb(bot_token, id, "Chat wasn't added!")

                         naziv = upd["message"]["chat"]["title"]
                         if naziv in group_name:
                             if "text" in upd["message"]:
                                 text = upd["message"]["text"]
                                 send_message(bot_token, chat_id2, format(text))
                             else:
                                 if "photo" in upd["message"]:
                                     if nfsb == 0:
                                         nfsb = 1
                                     else:
                                         if "caption" in upd["message"]:
                                             cap = upd["message"]["caption"]
                                             pv = upd["message"]["photo"][0]["file_id"]
                                             send_pv(bot_token, chat_id2, pv, format(cap))
                                         else:
                                             cap = ''
                                             pv = upd["message"]["photo"][0]["file_id"]
                                             send_pv(bot_token, chat_id2, pv, format(cap))
