from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8345730778:AAECxPUfD47cmjtRmaC8EiI7JWyjSALYYMI"

menu = [["📝 Ariza", "📞 Boglanish"]]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup(menu, resize_keyboard=True)
    await update.message.reply_text("Assalomu alaykum!", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if "Ariza" in text:
        await update.message.reply_text("Ismingizni yozing:")
    elif "Boglanish" in text:
        await update.message.reply_text("📞 Telefon: +998945051515")
    else:
        await update.message.reply_text("Tugmadan foydalaning")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot ishlayapti...")
app.run_polling()
