from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler
)

NAME, PHONE = range(2)

TOKEN = "8345730778:AAEh4BmVsw1GkDoecscU19bVWEMihk0ldT8"
ADMIN_ID = 775293298

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🚗 Avto sug‘urta"],
        ["📞 Aloqa", "ℹ️ Ma’lumot"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "👋 Salom!\nSug‘urta botga xush kelibsiz.\nKerakli bo‘limni tanlang 👇",
        reply_markup=reply_markup
    )

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🚗 Avto sug‘urta":
        await update.message.reply_text("Ismingizni kiriting:")
        return NAME

    elif text == "📞 Aloqa":
        await update.message.reply_text("Operator: +998 94 505 15 15")

    elif text == "ℹ️ Ma’lumot":
        await update.message.reply_text("Biz sizga eng yaxshi sug‘urta xizmatini taklif qilamiz.")

    return ConversationHandler.END


async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["name"] = update.message.text

    button = [[KeyboardButton("📞 Telefon raqamni yuborish", request_contact=True)]]
    await update.message.reply_text(
        "Telefon raqamingizni yuboring:",
        reply_markup=ReplyKeyboardMarkup(button, resize_keyboard=True)
    )

    return PHONE


async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = context.user_data.get("name")

    phone = update.message.contact.phone_number if update.message.contact else update.message.text

    text = f"🚗 Yangi avto sug‘urta ariza:\n\nIsm: {name}\nTelefon: {phone}"

    await context.bot.send_message(chat_id=ADMIN_ID, text=text)

    await update.message.reply_text("Arizangiz qabul qilindi ✅")

    return ConversationHandler.END


app = ApplicationBuilder().token(TOKEN).build()

conv = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex("^🚗 Avto sug‘urta$"), handle_menu)],
    states={
        NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
        PHONE: [MessageHandler(filters.CONTACT | filters.TEXT, get_phone)],
    },
    fallbacks=[CommandHandler("start", start)]
)

app.add_handler(CommandHandler("start", start))
app.add_handler(conv)
app.add_handler(MessageHandler(filters.Regex("^(📞 Aloqa|ℹ️ Ma’lumot)$"), handle_menu))

app.run_polling()
