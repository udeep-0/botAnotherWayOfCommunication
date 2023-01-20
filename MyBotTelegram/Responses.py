

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "Hey! How it going?"

    if user_message in ("who are you", "who are you?"):
        return "this is Dude bot"

    if user_message in ("time", "time?"):
        return "https://t.me/lyxuxixkxjxizkz463"

    return "i don't understand "
