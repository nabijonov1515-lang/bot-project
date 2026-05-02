from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8345730778:AAECxPUfD47cmjtRmaC8EiI7JWyjSALYYMI"

menu = [["📝 Ariza", "📞 Bog'lanish"]]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup(menu, resize_keyboard=True)
    await update.message.reply_text("Assalomu alaykum!", reply_markup=reply_markup)

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📝 Ariza":
        await update.message.reply_text("Ismingizni yozing:")
    elif text == "📞 Bog'lanish":
        await update.message.reply_text("📞 Telefon: +998945051515")
    else:
        await update.message.reply_text("Tugmadan foydalaning")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, message_handler))

print("Bot ishlayapti...")
app.run_polling()
