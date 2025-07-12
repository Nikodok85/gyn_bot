
from flask import Flask, request
import requests
import os

app = Flask(__name__)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

@app.route(f'/{BOT_TOKEN}', methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data and "text" in data["message"]:
        text = data["message"]["text"]
        send_message(f"❓ Анонимный вопрос: «{text}»")
    return {"ok": True}

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHANNEL_ID, "text": text}
    requests.post(url, json=payload)

@app.route('/')
def index():
    return "Bot is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
