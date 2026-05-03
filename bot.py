import telebot
from telebot import types

TOKEN = "8345730778:AAECxPUfD47cmjtRmaC8EiI7JWyjSALYYMI"
ADMIN_ID = 775293298

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📄 Ariza yuborish")
    markup.add(btn1)

    bot.send_message(message.chat.id, "Quyidagi tugmani bosing:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "📄 Ariza yuborish")
def ariza(message):
    bot.send_message(message.chat.id, "Arizangizni yozing:")

@bot.message_handler(func=lambda message: True)
def handle(message):
    bot.send_message(message.chat.id, "Ariza qabul qilindi ✅")
    bot.send_message(ADMIN_ID, f"Yangi ariza:\n\n{message.text}")

bot.infinity_polling()
