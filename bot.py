from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8345730778:AAECxPUfD47cmjtRmaC8EiI7JWyjSALYYMI"

menu = [["📝 Ariza", "📞 Boglanish"]]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum!",
        reply_markup=ReplyKeyboardMarkup(menu, resize_keyboard=True)
    )

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📝 Ariza":
        await update.message.reply_text("Ismingizni yozing:")
        context.user_data["step"] = "name"

    elif text == "📞 Boglanish":
        await update.message.reply_text("📞 Telefon: +998901234567")

    elif context.user_data.get("step") == "name":
        context.user_data["name"] = text
        context.user_data["step"] = "phone"
        await update.message.reply_text("Telefon raqamingizni yozing:")

    elif context.user_data.get("step") == "phone":
        name = context.user_data.get("name")
        phone = text

        await update.message.reply_text("✅ Arizangiz qabul qilindi!")

        context.user_data.clear()

    else:
        await update.message.reply_text("Iltimos tugmalardan foydalaning")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

print("Bot ishlayapti...")
app.run_polling()
