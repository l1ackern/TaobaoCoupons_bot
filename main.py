import time
import random
import telegram
from telegram.ext import Updater, CallbackContext
from flask import Flask

# Flask 用于保持 Railway 运行
app = Flask(__name__)

# 读取环境变量（Railway 部署时填写）
import os
BOT_TOKEN = os.getenv("7644254528:AAHiXaO8dzKf7wWTwaOmwpyiMTBvnH9CoZY")
CHANNEL_ID = os.getenv("-1002057590529")

# 商品列表（可自行修改）
products = [
    {"title": "🔥 限时福利！免费领取，薅羊毛别错过！", "url": "https://example.com/product1"},
    {"title": "💰 0元购！全程免费，速来领取！", "url": "https://example.com/product2"},
    {"title": "🚀 最新羊毛，免费拿！带引流神器！", "url": "https://example.com/product3"},
    {"title": "💎 独家福利，0成本享受！快来薅羊毛！", "url": "https://example.com/product4"}
]

def send_product():
    """定时推送商品到 Telegram 频道"""
    bot = telegram.Bot(token=BOT_TOKEN)
    product = random.choice(products)
    message = f"{product['title']}\n🔗 {product['url']}"
    bot.send_message(chat_id=CHANNEL_ID, text=message)

@app.route("/")
def home():
    return "Telegram Bot Running!"

if __name__ == "__main__":
    while True:
        send_product()
        time.sleep(600)  # 每 10 分钟推送一次
