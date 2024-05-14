import sys


class Notepad:
    def __init__(self, author: str, file_name: str) -> None:
        self.author = author
        self._file_name = file_name

    def _show_instructions(self) -> None:
        print(f"Welcome to Notepad, {self.author}")
        print("Commands: ")
        print("1. Add a new note")
        print("2. Display all notes")
        print("0. Exit Notepad")

    def _write_note(self) -> None:
        user_input: str = input("Enter your note: ")

        with open(f"{self._file_name}.txt", "w") as note:
            note.write(user_input)

        print("Bot: Added note")

    def _display_notes(self) -> None:
        try:
            with open(self._file_name, "r") as note:
                text: str = note.read()
                print(f"Bot: {text}")
        except FileNotFoundError:
            print("Bot: You need to write a note first!")

    def _exit_notepad(self) -> None:
        print(f"Goodbye {self.author}!")
        sys.exit()

    def run(self):
        self._show_instructions()
        while True:
            user_input: str = input(f"{self.author}: ")
            if user_input not in ("0", "1", "2"):
                print("Bot: Invalid input!")
                continue
            if user_input == "1":
                self._write_note()
            elif user_input == "2":
                self._display_notes()
            elif user_input == "0":
                self._exit_notepad()
            else:
                print(f"Bot: Invalid input: {user_input}")


def main() -> None:
    notepad: Notepad = Notepad("Vincent", "notepad")
    notepad.run()


if __name__ == "__main__":
    main()
