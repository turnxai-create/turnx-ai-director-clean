import os
from flask import Flask, request

import telegram
from handlers import handle_callback, handle_text

BOT_TOKEN = os.environ.get("BOT_TOKEN")

telegram.init(BOT_TOKEN)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "TURNX AI Director V4 is LIVE 🚀"


@app.route("/webhook", methods=["POST"])
def webhook():

    update = request.get_json(force=True)

    if not update:
        return "ok"

    # -------------------------
    # Callback Buttons
    # -------------------------

    if "callback_query" in update:

        callback = update["callback_query"]

        telegram.answer_callback(callback["id"])

        handle_callback(
            user_id=callback["from"]["id"],
            chat_id=callback["message"]["chat"]["id"],
            data=callback["data"]
        )

        return "ok"

    # -------------------------
    # Messages
    # -------------------------

    if "message" in update:

        message = update["message"]

        chat_id = message["chat"]["id"]

        user_id = message["from"]["id"]

        text = message.get("text", "")

        if text == "/start":

            telegram.home_menu(chat_id)

            return "ok"

        handle_text(
            user_id=user_id,
            chat_id=chat_id,
            text=text
        )

        return "ok"

    return "ok"


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
