import sys
from datetime import datetime


def get_response(text: str) -> str:
    lowered = text.lower()
    if lowered in ['hello', 'hi', 'hey', 'hii', 'hello there']:
        return 'Hey there!'
    elif "how are you today?" in lowered:
        return "I'm good thanks!"
    elif "your name" in lowered:
        return "My name is SUPER_BOT69"
    elif "time" in lowered:
        current_time = datetime.now()
        return f"It is {current_time:%H:%M} now!"
    elif lowered in ["bye", "goodbye"]:
        return "It was nice talking to you!"
    elif lowered in ["israel", "palestine", "ukraine", "russia"]:
        return "I won't answer anything related to any wars. All I can say though is free Palestine and Ukraine."
    else:
        return f"I didn't understand '{text}', I'm very sorry."


def bot_interaction():
    user_name = input("Bot: What is your name?: ")
    print(f"Bot: Welcome {user_name}!")

    while True:
        conversation_input = input(f"Bot: What do you want to talk about today, {user_name}? ")

        if conversation_input.lower() == "exit":
            print("Bot: It was a pleasure talking to you!")
            sys.exit()
        else:
            bot_response = get_response(conversation_input)
            print(f"Bot: {bot_response}")


# Start the conversation
bot_interaction()
