import os
from groq import Groq

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

MODEL = os.environ.get(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)

client = Groq(api_key=GROQ_API_KEY)


SYSTEM_PROMPT = """
You are TURNX AI Director.

You are NOT a chatbot.

You are an award-winning AI Creative Director.

You help creators build professional AI productions.

The only generation modes are:

1. Images

Supported image models:

- Nano Banana Pro 2
- Nano Banana Pro
- ChatGPT Image 2.0

2. Video

Supported models:

- Veo 3.1
- Omni
- Seedance
- Grok

3. Image to Video

Supported models:

- Veo 3.1
- Omni
- Seedance
- Grok

Never recommend any other AI model.

Always optimize prompts for the selected model.

Think like a creative director.

Plan first.

Generate second.

Every output must feel premium.
""" 
def ask_ai(user_prompt):

    response = client.chat.completions.create(

        model=MODEL,

        messages=[

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": user_prompt
            }

        ],

        temperature=0.8

    )

    return response.choices[0].message.content
  def image_prompt(model, idea):

    prompt = f"""
Create a professional AI image prompt.

Model:

{model}

Idea:

{idea}

Requirements:

- Ultra realistic
- Real skin texture
- Natural lighting
- Professional composition
- Character consistency
- Optimized specifically for {model}

Return ONLY the prompt.
"""

    return ask_ai(prompt)
    def video_prompt(model, idea):

    prompt = f"""
Create a professional AI video prompt.

Video Model:

{model}

Idea:

{idea}

Return:

Hook

Scene

Camera

Movement

Dialogue

Lighting

Cinematic details

Optimized specifically for {model}.
"""

    return ask_ai(prompt)
    def image_to_video_prompt(model, idea):

    prompt = f"""
Create one professional Image to Video prompt.

Video Model:

{model}

Idea:

{idea}

Include:

Camera movement

Character movement

Timing

Dialogue

Scene transitions

Keep identity consistent.

Optimized for {model}.

Return ONLY the prompt.
"""

    return ask_ai(prompt)
