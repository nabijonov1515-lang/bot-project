import telebot

TOKEN = "8345730778:AAECxPUfD47cmjtRmaC8EiI7JWyjSALYYMI"
ADMIN_ID = 775293298

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Ariza yuboring")

@bot.message_handler(func=lambda message: True)
def handle(message):
    # foydalanuvchiga javob
    bot.send_message(message.chat.id, "Ariza qabul qilindi ✅")

    # SENGA yuboradi (ENG MUHIM QISM)
    bot.send_message(ADMIN_ID, f"Yangi ariza:\n\n{message.text}")

bot.polling()
