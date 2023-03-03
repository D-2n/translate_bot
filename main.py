import telebot as tb
import time
TOKEN = '5259610624:AAGMNZmwTmX00LGno0Ykn8MiZMnVL4UK1zw'
bot=tb.TeleBot(TOKEN)
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"Peki")
while True:
    try:
        bot.polling()
    except:
        time.sleep(5)
