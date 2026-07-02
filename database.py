import json
import os

DB_FILE = "database.json"


def load_db():

    if not os.path.exists(DB_FILE):
        return {}

    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_db(data):

    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


def get_user(user_id):

    db = load_db()

    uid = str(user_id)

    if uid not in db:

        db[uid] = {
            "premium": False,
            "generations": 0,
            "character": "",
            "mode": "",
            "model": ""
        }

        save_db(db)

    return db[uid]


def update_user(user_id, values):

    db = load_db()

    uid = str(user_id)

    if uid not in db:
        db[uid] = {}

    db[uid].update(values)

    save_db(db)


def reset_generations():

    db = load_db()

    for uid in db:

        db[uid]["generations"] = 0

    save_db(db)
