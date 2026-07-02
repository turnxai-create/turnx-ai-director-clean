import json
import os

CHARACTER_FILE = "characters.json"


def _load():

    if not os.path.exists(CHARACTER_FILE):
        return {}

    with open(CHARACTER_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(data):

    with open(CHARACTER_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def save_character(user_id, description):

    data = _load()

    data[str(user_id)] = {
        "description": description
    }

    _save(data)


def get_character(user_id):

    data = _load()

    return data.get(
        str(user_id),
        {}
    ).get(
        "description",
        ""
    )


def has_character(user_id):

    return get_character(user_id) != ""


def clear_character(user_id):

    data = _load()

    uid = str(user_id)

    if uid in data:

        del data[uid]

        _save(data)


def build_character_prompt(user_id):

    character = get_character(user_id)

    if not character:

        return ""

    return f"""

CHARACTER LOCK

Maintain this exact identity across every generated image.

Never change:

- Face
- Skin tone
- Hair
- Facial proportions
- Age
- Body shape

Character Description:

{character}

This character must remain identical in every scene.
"""
