from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = '8027662725:AAEAydbYQxsA2Zbx0acgUlCzTgymzb4VBkM'
CHAT_ID = '6940287840'  # ID твоего Telegram-канала

@app.route('/')
def index():
    return 'Бот запущен!'

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    data = request.json
    if 'message' in data and 'text' in data['message']:
        text = data['message']['text']
        send_message(f"❓ Анонимный вопрос: «{text}»")
    return {'ok': True}

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': text
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run()
