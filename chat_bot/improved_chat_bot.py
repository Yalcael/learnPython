from datetime import datetime
from difflib import get_close_matches


class ChatBot:
    def __init__(self, knowledge: dict):
        self.knowledge = knowledge

    def get_best_match(self, user_input: str) -> str | None:
        questions = [q.lower() for q in self.knowledge.keys()]
        matches = get_close_matches(user_input, questions, n=1, cutoff=0.6)

        if matches:
            return matches[0]

    def get_response(self, user_input: str) -> str:
        user_input = user_input.lower()  # Convert to lowercase for case-insensitivity
        best_match = self.get_best_match(user_input)

        if best_match:
            return self.knowledge[best_match]
        else:
            return "Sorry, I couldn't understand that. Please try again."


def main() -> None:
    knowledge = {
        "hello": "world",
        "goodbye": "world",
        "how are you?": "I am fine",
        "how are you doing": "I am fine",
        "do you know what the time is?": f"The current time is {datetime.now():%H:%M:%S}",
        "what can you do?": "I can answer questions!",
        "ok": "Great."
    }

    bot = ChatBot(knowledge)
    while True:
        user_input = input("Your question: ")
        if user_input:
            if user_input == "exit":
                print(f"Thank you for chatting with me OwO!")
                break
            response = bot.get_response(user_input)
            print(f"Bot : {response}")
        else:
            print("Sorry, I couldn't understand that. Please try again.")


if __name__ == '__main__':
    main()


# from difflib import get_close_matches, SequenceMatcher
# from datetime import datetime
#
#
# class BestMatch:
#     def __init__(self, user_question: str, knowledge: dict) -> None:
#         self.user_question = user_question
#         self.knowledge = knowledge
#
#     def get_best_match(self) -> str | None:
#         questions: list[str] = [q for q in self.knowledge]
#         matches: list[str] = get_close_matches(self.user_question, questions, n=1)
#
#         if matches:
#             best_match = matches[0]
#             if SequenceMatcher(None, self.user_question, best_match).ratio() > 0.6:
#                 return best_match
#
#
# class ChatBot(BestMatch):
#     def __init__(self, user_question: str, knowledge: dict):
#         super().__init__(user_question, knowledge)
#
#     def run(self):
#         while True:
#             user_input: str = input("Your question: ")
#
#             best_match: BestMatch = BestMatch(user_input, self.knowledge)
#             match: str = best_match.get_best_match()
#
#             if match:
#                 response = self.knowledge[match]
#                 print(f"Bot : {response}")
#             else:
#                 print(f"Bot: Sorry, I couldn't understand that. Please try again.")
#
#
# def main() -> None:
#     now: datetime = datetime.now()
#     knowledge: dict[str, str] = {"hello": "world",
#                                  "goodbye": "world",
#                                  "how are you?": "I am fine",
#                                  "how are you doing": "I am fine",
#                                  "do you know what the time is?": f"The current time is {now:%H:%M:%S}",
#                                  "what can you do?": "I can answer questions!",
#                                  "ok": "Great."}
#     bot: ChatBot = ChatBot("", knowledge)
#     bot.run()
#
#
# if __name__ == '__main__':
#     main()
