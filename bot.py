from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8345730778:AAECxPUfD47cmjtRmaC8EiI7JWyjSALYYMI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Bot ishlayapti 🚀")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot ishlayapti...")
app.run_polling()
