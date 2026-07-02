import json
import os

MEMORY_FILE = "memory.json"


def _load():
    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def get_memory(user_id):

    data = _load()

    uid = str(user_id)

    if uid not in data:

        data[uid] = {

            "image_model": "",

            "video_model": "",

            "i2v_model": "",

            "character_lock": "",

            "brand_name": "",

            "language": "English",

            "country": "",

            "premium": False,

            "daily_generations": 0

        }

        _save(data)

    return data[uid]


def update_memory(user_id, key, value):

    data = _load()

    uid = str(user_id)

    if uid not in data:

        get_memory(user_id)

        data = _load()

    data[uid][key] = value

    _save(data)


def reset_daily_generations():

    data = _load()

    for uid in data:

        data[uid]["daily_generations"] = 0

    _save(data)


def add_generation(user_id):

    data = _load()

    uid = str(user_id)

    if uid not in data:

        get_memory(user_id)

        data = _load()

    data[uid]["daily_generations"] += 1

    _save(data)


def is_premium(user_id):

    return get_memory(user_id)["premium"]


def set_premium(user_id, value=True):

    update_memory(user_id, "premium", value)
