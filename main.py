import telebot
import os
from flask import Flask, request

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Бот работает ✅ Напиши свой анонимный вопрос.")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def forward_message(message):
    if message.chat.type == "private":
        bot.send_message(CHANNEL_ID, f"❓ Анонимный вопрос: «{message.text}»")

@app.route('/' + BOT_TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f"https://gyn-bot.onrender.com/{BOT_TOKEN}")
    return "!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
