# User conversation state

users = {}


def set_state(user_id, state):
    users.setdefault(user_id, {})
    users[user_id]["state"] = state


def get_state(user_id):
    return users.get(user_id, {}).get("state")


def clear_state(user_id):
    if user_id in users:
        users[user_id]["state"] = None


def set_data(user_id, key, value):
    users.setdefault(user_id, {})
    users[user_id][key] = value


def get_data(user_id, key, default=None):
    return users.get(user_id, {}).get(key, default)
