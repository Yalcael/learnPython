import sys
from datetime import datetime


def get_response(text: str) -> str:
    lowered = text.lower()
    if lowered in ['hello', 'hi', 'hey', 'hii', 'hello there']:
        return 'Hey there!'
    elif "how are you today?" in lowered:
        return "I'm good thanks!"
    elif "your name" in lowered:
        return "My name is SUPERBOT69"
    elif "time" in lowered:
        current_time : datetime = datetime.now()
        return f"it is {current_time:%H:%M} now!"
    elif lowered in ["bye", "byebye", "Goodbye"]:
        return "It was nice talking to you!!"
    elif lowered in ["Israel", "Palestine", "Ukraine", "Russia"]:
        return f"I won't answer anything relate to any wars. All I can say tho it's free Palestine and Ukraine."
    else:
        return f"I didn't understand {text}, i'm very sorry."


while True:
    user_input: str = input(f"You: ")

    if user_input == "exit":
        print("Bot: It was a pleasure talking to you!")
        sys.exit()

    bot_response: str = get_response(user_input)
    print(f" Bot said: \n{bot_response}")
