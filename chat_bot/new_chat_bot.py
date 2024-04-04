from random import choice
from datetime import datetime


class ChatBot:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_description(self) -> str:
        return f"{self.name} is a bot who is {self.age} years old."

    def get_response(self, text: str) -> str:
        lowered: str = text.lower()

        if "hello" in lowered:
            return f"{self.name}: Hey there!"
        elif "bye" in lowered:
            return f"{self.name}: See you!"
        elif "how old are you" in lowered:
            return f"{self.name}: I am {self.age} years old!"
        elif "what time is it" in lowered:
            now: datetime = datetime.now()
            return f"{self.name}: The current time is {now:%H:%M:%S}"
        elif "how are you" in lowered:
            return f"{self.name}: Great, thanks!"
        else:
            random_response: list[str] = ["I don't understand...", "Can you repeat please?", "Explain with words that I actually know please..."]
            return f"{self.name}: {choice(random_response)}"

    def run(self) -> None:
        while True:
            user_input: str = input("You: ")
            if user_input == "exit":
                print(f"Thank you for chatting with {self.name}")
                break
            response: str = self.get_response(user_input)
            print(response)


def main() -> None:
    vincent: ChatBot = ChatBot("Vincent", 24)
    print(vincent.get_description())
    vincent.run()


if __name__ == "__main__":
    main()
