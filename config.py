import os

# ==========================
# API Keys
# ==========================

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

# ==========================
# AI Model
# ==========================

GROQ_MODEL = os.environ.get(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)

# ==========================
# TURNX MODELS
# ==========================

IMAGE_MODELS = [

    "Nano Banana Pro 2",

    "Nano Banana Pro",

    "ChatGPT Image 2.0"

]

VIDEO_MODELS = [

    "Veo 3.1",

    "Omni",

    "Seedance",

    "Grok"

]

IMAGE_TO_VIDEO_MODELS = [

    "Veo 3.1",

    "Omni",

    "Seedance",

    "Grok"

]

# ==========================
# Free Plan
# ==========================

FREE_GENERATIONS_PER_DAY = 3

# ==========================
# Premium
# ==========================

PREMIUM_PRICE_STARS = 250

PREMIUM_DAYS = 30

# ==========================
# TURNX
# ==========================

BOT_NAME = "TURNX AI Director"

VERSION = "V4"
