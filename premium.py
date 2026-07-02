import json
import os
from datetime import datetime, timedelta

PREMIUM_FILE = "premium.json"

FREE_LIMIT = 3

PREMIUM_DAYS = 30


def _load():

    if not os.path.exists(PREMIUM_FILE):
        return {}

    with open(PREMIUM_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(data):

    with open(PREMIUM_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def is_premium(user_id):

    data = _load()

    uid = str(user_id)

    if uid not in data:
        return False

    expires = data[uid]["expires"]

    return datetime.utcnow() <= datetime.fromisoformat(expires)


def activate_premium(user_id, days=PREMIUM_DAYS):

    data = _load()

    uid = str(user_id)

    expires = datetime.utcnow() + timedelta(days=days)

    data[uid] = {

        "active": True,

        "expires": expires.isoformat()

    }

    _save(data)


def remaining_days(user_id):

    if not is_premium(user_id):
        return 0

    data = _load()

    expires = datetime.fromisoformat(
        data[str(user_id)]["expires"]
    )

    return max(
        0,
        (expires - datetime.utcnow()).days
    )


def can_generate(user_memory):

    if user_memory.get("premium", False):
        return True

    return user_memory.get(
        "daily_generations",
        0
    ) < FREE_LIMIT


def generations_left(user_memory):

    if user_memory.get("premium", False):
        return "Unlimited"

    left = FREE_LIMIT - user_memory.get(
        "daily_generations",
        0
    )

    return max(0, left)


def upgrade_text():

    return """
⭐ TURNX AI Director Premium

Unlock:

✅ Unlimited prompt generations

✅ Priority AI optimization

✅ Advanced prompt engine

✅ Full workflow generation

✅ Future TURNX upgrades

Subscription:

30 Days Premium
"""
