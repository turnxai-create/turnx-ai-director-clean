import json
import requests
from ai import image_prompt, video_prompt, image_to_video_prompt

# In-memory state (replace with database later)
users = {}

BOT_TOKEN = None

def init(bot_token):
    global BOT_TOKEN
    BOT_TOKEN = bot_token

def api(method):
    return f"https://api.telegram.org/bot{BOT_TOKEN}/{method}"

def send_message(chat_id, text, keyboard=None):
    payload = {"chat_id": chat_id, "text": text}
    if keyboard:
        payload["reply_markup"] = json.dumps({"inline_keyboard": keyboard})
    requests.post(api("sendMessage"), json=payload)

def answer_callback(callback_id):
    requests.post(api("answerCallbackQuery"),
                  json={"callback_query_id": callback_id})

def home_menu(chat_id):
    kb = [
        [{"text":"🖼 Images","callback_data":"images"}],
        [{"text":"🎥 Video","callback_data":"video"}],
        [{"text":"🔄 Image → Video","callback_data":"i2v"}],
        [{"text":"⭐ Upgrade","callback_data":"upgrade"}],
        [{"text":"⚙ Settings","callback_data":"settings"}],
    ]
    send_message(chat_id,"🎬 TURNX AI Director\n\nChoose a generation mode.",kb)

def image_models(chat_id):
    kb=[
      [{"text":"Nano Banana Pro 2","callback_data":"img:banana2"}],
      [{"text":"Nano Banana Pro","callback_data":"img:banana"}],
      [{"text":"ChatGPT Image 2.0","callback_data":"img:chatgpt"}],
      [{"text":"⬅ Back","callback_data":"home"}]
    ]
    send_message(chat_id,"Choose an image model.",kb)

def video_models(chat_id):
    kb=[
      [{"text":"Veo 3.1","callback_data":"vid:veo31"}],
      [{"text":"Omni","callback_data":"vid:omni"}],
      [{"text":"Seedance","callback_data":"vid:seedance"}],
      [{"text":"Grok","callback_data":"vid:grok"}],
      [{"text":"⬅ Back","callback_data":"home"}]
    ]
    send_message(chat_id,"Choose a video model.",kb)

def i2v_models(chat_id):
    kb=[
      [{"text":"Veo 3.1","callback_data":"i2v:veo31"}],
      [{"text":"Omni","callback_data":"i2v:omni"}],
      [{"text":"Seedance","callback_data":"i2v:seedance"}],
      [{"text":"Grok","callback_data":"i2v:grok"}],
      [{"text":"⬅ Back","callback_data":"home"}]
    ]
    send_message(chat_id,"Choose an Image → Video model.",kb)

def handle_callback(callback):
    answer_callback(callback["id"])
    chat_id=callback["message"]["chat"]["id"]
    uid=callback["from"]["id"]
    data=callback["data"]

    if data=="home":
        return home_menu(chat_id)
    if data=="images":
        return image_models(chat_id)
    if data=="video":
        return video_models(chat_id)
    if data=="i2v":
        return i2v_models(chat_id)

    if data.startswith("img:"):
        users[uid]={"mode":"image","model":data.split(":")[1]}
        return send_message(chat_id,"Send your image idea.")

    if data.startswith("vid:"):
        users[uid]={"mode":"video","model":data.split(":")[1]}
        return send_message(chat_id,"Send your video idea.")

    if data.startswith("i2v:"):
        users[uid]={"mode":"i2v","model":data.split(":")[1]}
        return send_message(chat_id,"Send your image-to-video idea.")

def handle_message(message):
    chat_id=message["chat"]["id"]
    uid=message["from"]["id"]
    text=message.get("text","")

    if text=="/start":
        return home_menu(chat_id)

    if uid not in users:
        return send_message(chat_id,"Send /start")

    info=users.pop(uid)
    if info["mode"]=="image":
        out=image_prompt(info["model"],text)
    elif info["mode"]=="video":
        out=video_prompt(info["model"],text)
    else:
        out=image_to_video_prompt(info["model"],text)
    send_message(chat_id,out)
