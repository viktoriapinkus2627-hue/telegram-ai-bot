import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("📘 Получить AI гайд", callback_data="guide")],
        [InlineKeyboardButton("🌐 Открыть Telegram канал", url="https://t.me/ai_freelance_startgo")],
        [InlineKeyboardButton("📩 Связаться", callback_data="contact")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Привет! 👋\n\n"
        "Я бот, который отправит тебе бесплатный AI гайд.\n\n"
        "Нажми кнопку ниже:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "guide":

        await query.message.reply_text(
            "Вот твой AI гайд:\n"
            "https://drive.google.com"
        )

    if query.data == "contact":

        await query.message.reply_text(
            "Мой Telegram:\n"
            "https://t.me/ai_freelance_startgo"
        )

def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("БОТ ЗАПУЩЕН")

    app.run_polling()

if __name__ == "__main__":
    main()
