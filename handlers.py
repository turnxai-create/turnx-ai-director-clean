from telegram import (
    home_menu,
    image_models,
    video_models,
    i2v_models,
    send_message
)

from states import (
    set_state,
    get_state,
    set_data,
    get_data,
    clear_state
)

from director import director


def handle_callback(user_id, chat_id, data):

    if data == "home":
        home_menu(chat_id)
        return

    if data == "images":
        image_models(chat_id)
        return

    if data == "video":
        video_models(chat_id)
        return

    if data == "i2v":
        i2v_models(chat_id)
        return

    if data.startswith("img:"):

        model = data.replace("img:", "")

        set_data(user_id, "mode", "image")
        set_data(user_id, "model", model)

        set_state(user_id, "WAITING_IDEA")

        send_message(
            chat_id,
            "📸 Send your image idea."
        )

        return

    if data.startswith("vid:"):

        model = data.replace("vid:", "")

        set_data(user_id, "mode", "video")
        set_data(user_id, "model", model)

        set_state(user_id, "WAITING_IDEA")

        send_message(
            chat_id,
            "🎥 Send your video idea."
        )

        return

    if data.startswith("i2v:"):

        model = data.replace("i2v:", "")

        set_data(user_id, "mode", "i2v")
        set_data(user_id, "model", model)

        set_state(user_id, "WAITING_IDEA")

        send_message(
            chat_id,
            "🔄 Send your Image → Video idea."
        )

        return


def handle_text(user_id, chat_id, text):

    state = get_state(user_id)

    if state != "WAITING_IDEA":

        send_message(
            chat_id,
            "Use /start to begin."
        )

        return

    mode = get_data(user_id, "mode")

    model = get_data(user_id, "model")

    send_message(
        chat_id,
        "🧠 TURNX Director is creating your prompt..."
    )

    result = director.generate(
        user_id=user_id,
        mode=mode,
        model=model,
        idea=text
    )

    send_message(
        chat_id,
        result
    )

    clear_state(user_id)
