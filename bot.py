from flask import Flask, request
import os
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, filters

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is running!'

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

def echo(update, context):
    context.bot.send_message(chat_id=CHANNEL_ID, text=f"❓ Анонимный вопрос: «{update.message.text}»")

from telegram.ext import CommandHandler, MessageHandler, Filters
dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))