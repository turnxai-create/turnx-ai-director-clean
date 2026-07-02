import os
from flask import Flask, request

from telegram import (
    send_message,
    home_menu,
    image_models,
    video_models,
    image_to_video_models,
    answer_callback
)

from states import (
    set_state,
    get_state,
    set_data,
    get_data
)

from ai import (
    image_prompt,
    video_prompt,
    image_to_video_prompt
)

app = Flask(__name__)


@app.route("/")
def home():
    return "TURNX AI Director V4 is LIVE 🚀"


@app.route("/webhook", methods=["POST"])
def webhook():

    update = request.get_json()

    if not update:
        return "ok"

    # -------------------------
    # Button Clicks
    # -------------------------

    if "callback_query" in update:

        callback = update["callback_query"]

        answer_callback(callback["id"])

        chat_id = callback["message"]["chat"]["id"]

        user_id = callback["from"]["id"]

        data = callback["data"]

        if data == "home":
            home_menu(chat_id)

        elif data == "images":
            image_models(chat_id)

        elif data == "video":
            video_models(chat_id)

        elif data == "i2v":
            image_to_video_models(chat_id)

        elif data == "banana2":

            set_data(user_id, "mode", "image")
            set_data(user_id, "model", "Nano Banana Pro 2")
            set_state(user_id, "WAITING_FOR_IDEA")

            send_message(
                chat_id,
                "Describe what you want to create."
            )

        elif data == "banana":

            set_data(user_id, "mode", "image")
            set_data(user_id, "model", "Nano Banana Pro")
            set_state(user_id, "WAITING_FOR_IDEA")

            send_message(chat_id, "Describe your idea.")

        elif data == "chatgptimage":

            set_data(user_id, "mode", "image")
            set_data(user_id, "model", "ChatGPT Image 2.0")
            set_state(user_id, "WAITING_FOR_IDEA")

            send_message(chat_id, "Describe your idea.")

        elif data == "veo":

            set_data(user_id, "mode", "video")
            set_data(user_id, "model", "Veo 3.1")
            set_state(user_id, "WAITING_FOR_IDEA")

            send_message(chat_id, "Describe your video idea.")

        elif data == "omni":

            set_data(user_id, "mode", "video")
            set_data(user_id, "model", "Omni")
            set_state(user_id, "WAITING_FOR_IDEA")

            send_message(chat_id, "Describe your video idea.")

        elif data == "seedance":

            set_data(user_id, "mode", "video")
            set_data(user_id, "model", "Seedance")
            set_state(user_id, "WAITING_FOR_IDEA")

            send_message(chat_id, "Describe your video idea.")

        elif data == "grok":

            set_data(user_id, "mode", "video")
            set_data(user_id, "model", "Grok")
            set_state(user_id, "WAITING_FOR_IDEA")

            send_message(chat_id, "Describe your video idea.")

        return "ok"

    # -------------------------
    # Messages
    # -------------------------

    message = update.get("message")

    if not message:
        return "ok"

    chat_id = message["chat"]["id"]

    user_id = message["from"]["id"]

    text = message.get("text", "")

    if text == "/start":

        home_menu(chat_id)

        return "ok"

    state = get_state(user_id)

    if state == "WAITING_FOR_IDEA":

        model = get_data(user_id, "model")

        mode = get_data(user_id, "mode")

        send_message(chat_id, "🧠 TURNX Director is working...")

        if mode == "image":

            result = image_prompt(model, text)

        elif mode == "video":

            result = video_prompt(model, text)

        else:

            result = image_to_video_prompt(model, text)

        send_message(chat_id, result)

        return "ok"

    send_message(chat_id, "Send /start")

    return "ok"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
            )
