from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

TOKEN = "8345730778:AAECxPUfD47cmjtRmaC8EiI7JWyjSALYYMI"
ADMIN_ID = 775293298  # o'z telegram id'ing

ISM, TEL = range(2)

menu = [["📝 Ariza yuborish", "📞 Bog'lanish"]]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup(menu, resize_keyboard=True)
    await update.message.reply_text("Assalomu alaykum!\nSug'urta botiga xush kelibsiz", reply_markup=reply_markup)

async def ariza(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ismingizni kiriting:")
    return ISM

async def ism(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["ism"] = update.message.text
    await update.message.reply_text("Telefon raqamingizni kiriting:")
    return TEL

async def tel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["tel"] = update.message.text

    text = f"🆕 Yangi ariza!\n\n👤 Ism: {context.user_data['ism']}\n📞 Tel: {context.user_data['tel']}"

    await context.bot.send_message(chat_id=ADMIN_ID, text=text)

    await update.message.reply_text("✅ Arizangiz qabul qilindi!")

    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bekor qilindi")
    return ConversationHandler.END

async def boglanish(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📞 Telefon: +998945051515")

def main():
    app = Application.builder().token(TOKEN).build()

    conv = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("📝 Ariza yuborish"), ariza)],
        states={
            ISM: [MessageHandler(filters.TEXT & ~filters.COMMAND, ism)],
            TEL: [MessageHandler(filters.TEXT & ~filters.COMMAND, tel)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv)
    app.add_handler(MessageHandler(filters.Regex("📞 Bog'lanish"), boglanish))

    print("Bot ishlayapti...")
    app.run_polling()

if name == "main":
    main()
