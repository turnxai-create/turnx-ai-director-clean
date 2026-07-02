import json
import requests
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

API = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_message(chat_id, text, keyboard=None):

    payload = {
        "chat_id": chat_id,
        "text": text
    }

    if keyboard:
        payload["reply_markup"] = json.dumps({
            "inline_keyboard": keyboard
        })

    requests.post(
        f"{API}/sendMessage",
        json=payload
    )


def answer_callback(callback_id):

    requests.post(
        f"{API}/answerCallbackQuery",
        json={
            "callback_query_id": callback_id
        }
    )


def home_menu(chat_id):

    keyboard = [

        [
            {
                "text": "🖼 Images",
                "callback_data": "images"
            }
        ],

        [
            {
                "text": "🎥 Video",
                "callback_data": "video"
            }
        ],

        [
            {
                "text": "🔄 Image → Video",
                "callback_data": "i2v"
            }
        ],

        [
            {
                "text": "⭐ Upgrade",
                "callback_data": "upgrade"
            }
        ],

        [
            {
                "text": "⚙ Settings",
                "callback_data": "settings"
            }
        ]

    ]

    send_message(

        chat_id,

        """🎬 TURNX AI Director

Select what you want to generate.

Everything is professionally directed for AI content creation.

Choose a mode below.""",

        keyboard

    )


def image_models(chat_id):

    keyboard = [

        [
            {
                "text": "Nano Banana Pro 2",
                "callback_data": "banana2"
            }
        ],

        [
            {
                "text": "Nano Banana Pro",
                "callback_data": "banana"
            }
        ],

        [
            {
                "text": "ChatGPT Image 2.0",
                "callback_data": "chatgptimage"
            }
        ],

        [
            {
                "text": "⬅ Back",
                "callback_data": "home"
            }
        ]

    ]

    send_message(

        chat_id,

        "Choose your Image Model.",

        keyboard

    )


def video_models(chat_id):

    keyboard = [

        [
            {
                "text": "Veo 3.1",
                "callback_data": "veo"
            }
        ],

        [
            {
                "text": "Omni",
                "callback_data": "omni"
            }
        ],

        [
            {
                "text": "Seedance",
                "callback_data": "seedance"
            }
        ],

        [
            {
                "text": "Grok",
                "callback_data": "grok"
            }
        ],

        [
            {
                "text": "⬅ Back",
                "callback_data": "home"
            }
        ]

    ]

    send_message(

        chat_id,

        "Choose your Video Model.",

        keyboard

    )


def image_to_video_models(chat_id):

    keyboard = [

        [
            {
                "text": "Veo 3.1",
                "callback_data": "veo_i2v"
            }
        ],

        [
            {
                "text": "Omni",
                "callback_data": "omni_i2v"
            }
        ],

        [
            {
                "text": "Seedance",
                "callback_data": "seedance_i2v"
            }
        ],

        [
            {
                "text": "Grok",
                "callback_data": "grok_i2v"
            }
        ],

        [
            {
                "text": "⬅ Back",
                "callback_data": "home"
            }
        ]

    ]

    send_message(

        chat_id,

        "Choose your Image → Video Model.",

        keyboard

  )
