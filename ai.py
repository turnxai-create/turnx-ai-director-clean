# TURNX AI Director - ai.py
import os
from groq import Groq

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
MODEL = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """ You are TURNX AI Director. Only support: Images: - Nano Banana Pro 2 - Nano Banana Pro - ChatGPT Image 2.0 Video: - Veo 3.1 - Omni - Seedance - Grok Image to Video: - Veo 3.1 - Omni - Seedance - Grok Always optimize prompts for the selected model. """

def ask_ai(user_prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":user_prompt}
        ],
        temperature=0.8,
    )
    return response.choices[0].message.content

def image_prompt(model, idea):
    return ask_ai(f"""Create a production-quality image prompt. Model: {model} Idea: {idea} Return only the finished prompt. """)

def video_prompt(model, idea):
    return ask_ai(f"""Create a production-quality video prompt. Video Model: {model} Idea: {idea} Return: - Hook - Scene - Camera - Movement - Dialogue - Lighting - Final prompt """)

def image_to_video_prompt(model, idea):
    return ask_ai(f"""Create one professional image-to-video prompt. Video Model: {model} Idea: {idea} Include camera movement, subject movement, dialogue (if needed), timing, and consistency instructions. Return only the final prompt. """)
