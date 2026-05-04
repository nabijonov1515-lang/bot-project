from telebot import TeleBot, types
from flask import Flask
import threading
import os

TOKEN = os.environ.get("8762127280:AAFarO195M3tCMG5_RvkTwomhVxXsf14_bE")
ADMIN_ID = 775293298

bot = TeleBot(TOKEN)
app = Flask(name)

user_data = {}
user_ids = {}  # chat mapping

# ---------------- MENU ----------------

def main_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        types.KeyboardButton("📝 Ariza berish"),
        types.KeyboardButton("📞 Admin bilan bog'lanish")
    )

    bot.send_message(chat_id, "🏠 Asosiy menyu", reply_markup=markup)

# ---------------- START ----------------

@bot.message_handler(commands=['start'])
def start(message):
    user_ids[message.chat.id] = message.chat.id
    main_menu(message.chat.id)

# ---------------- ADMIN CHAT INFO ----------------

@bot.message_handler(func=lambda m: m.text == "📞 Admin bilan bog'lanish")
def admin_info(message):
    bot.send_message(message.chat.id,
"""📩 ADMIN

📞 +99894 505 15 15
📨 @uca212

📌 Bizda oldindan to‘lov YO‘Q.
📄 Sug‘urta polisi PDF shaklida yuboriladi.
💳 To‘lov hujjatni olgandan keyin amalga oshiriladi.
🏦 To‘lov karta orqali.

✍️ Savol bo‘lsa yozing.""")

# ---------------- ARIZA ----------------

@bot.message_handler(func=lambda m: m.text == "📝 Ariza berish")
def form_start(message):
    bot.send_message(message.chat.id, "👤 Ismingizni kiriting:")
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    user_data[message.chat.id] = {"name": message.text}

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("📱 Raqam yuborish", request_contact=True))

    bot.send_message(message.chat.id, "📱 Telefon raqam:", reply_markup=markup)
    bot.register_next_step_handler(message, get_phone)

def get_phone(message):
    phone = message.contact.phone_number if message.contact else message.text
    user_data[message.chat.id]["phone"] = phone

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton("🚗 Avto"),
        types.KeyboardButton("🏥 Med"),
        types.KeyboardButton("✈️ Travel")
    )

    bot.send_message(message.chat.id, "📄 Sug'urta turi:", reply_markup=markup)
    bot.register_next_step_handler(message, get_service)

def get_service(message):
    user_data[message.chat.id]["service"] = message.text
    data = user_data[message.chat.id]

    text = f"""
📥 YANGI ARIZA

👤 {data['name']}
📱 {data['phone']}
📄 {data['service']}
"""

    # send admin
    bot.send_message(ADMIN_ID, text)

    bot.send_message(message.chat.id, "✅ Ariza yuborildi!")

    main_menu(message.chat.id)

# ---------------- ADMIN REPLY SYSTEM ----------------

@bot.message_handler(func=lambda m: m.chat.id == ADMIN_ID and m.reply_to_message)
def admin_reply(message):
    text = message.text

    for user_id in user_data:
        bot.send_message(user_id, f"📩 Admin: {text}")
        return

# ---------------- FLASK (PING) ----------------

@app.route('/')
def home():
    return "Bot ishlayapti ✅"

def run_bot():
    bot.infinity_polling()

threading.Thread(target=run_bot).start()

app.run(host="0.0.0.0", port=5000)
