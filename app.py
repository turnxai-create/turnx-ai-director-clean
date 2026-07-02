import os
from flask import Flask, request
import telegram

BOT_TOKEN = os.environ.get("BOT_TOKEN")
telegram.init(BOT_TOKEN)

app = Flask(__name__)

@app.get("/")
def home():
    return "TURNX AI Director is LIVE"

@app.post("/webhook")
def webhook():
    update = request.get_json(force=True)

    if "callback_query" in update:
        telegram.handle_callback(update["callback_query"])
        return "ok"

    if "message" in update:
        telegram.handle_message(update["message"])
        return "ok"

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
