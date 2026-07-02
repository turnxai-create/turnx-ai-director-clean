from prompts import (
    image_master,
    video_master,
    image_to_video_master,
)

from character_lock import (
    build_character_prompt,
)

from ai import ask_ai


class TurnxDirector:

    def __init__(self):
        pass

    # ----------------------------
    # IMAGE
    # ----------------------------

    def generate_image(
        self,
        user_id,
        model,
        idea
    ):

        character = build_character_prompt(user_id)

        prompt = image_master(
            model=model,
            idea=idea
        )

        final_prompt = f"""
{character}

{prompt}
"""

        return ask_ai(final_prompt)

    # ----------------------------
    # VIDEO
    # ----------------------------

    def generate_video(
        self,
        user_id,
        model,
        idea
    ):

        prompt = video_master(
            model=model,
            idea=idea
        )

        return ask_ai(prompt)

    # ----------------------------
    # IMAGE → VIDEO
    # ----------------------------

    def generate_image_to_video(
        self,
        user_id,
        model,
        idea
    ):

        character = build_character_prompt(user_id)

        prompt = image_to_video_master(
            model=model,
            idea=idea
        )

        final_prompt = f"""
{character}

{prompt}
"""

        return ask_ai(final_prompt)

    # ----------------------------
    # ROUTER
    # ----------------------------

    def generate(
        self,
        user_id,
        mode,
        model,
        idea
    ):

        if mode == "image":

            return self.generate_image(
                user_id,
                model,
                idea
            )

        if mode == "video":

            return self.generate_video(
                user_id,
                model,
                idea
            )

        if mode == "i2v":

            return self.generate_image_to_video(
                user_id,
                model,
                idea
            )

        return "Unknown generation mode."


director = TurnxDirector()
