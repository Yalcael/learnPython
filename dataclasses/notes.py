from dataclasses import dataclass, field
from uuid import uuid4, UUID


@dataclass
class Note:
    id: UUID = field(init=False)
    title: str
    body: str

    def __post_init__(self) -> None:
        self.id = uuid4()


class NoteApp:
    def __init__(self, author: str, notes: list[Note] | None = None) -> None:
        self.author = author

        if notes is None:
            """
            if notes is None means that the use didn't insert anything. This check if the user has inserted notes or not.
            While initializing self.notes.
            We type _notes because we want this to be considered a private variable and it is equal to empty pair of square brackets so empty list. 
            The _ in front actually means is that this variable should not be used outside of the class.
            It was only made to be used within the class.
            """
            self._notes = []
        else:
            self._notes = notes

        self.display_instructions()

    @staticmethod
    def display_instructions() -> None:
        print("Welcome to Notes!")
        print("Here are the commands: ")
        print("1 - Add a new note")
        print("2 - Edit a note")
        print("3 - Delete a note")
        print("4 - Display all notes")
        print("5 - Display instructions")
        """
        It is a static method since it's not going to depend on the instance.
        """

    def _add_note(self) -> None:
        title: str = input("Title: ")
        body: str = input("Body: ")

        note: Note = Note(title, body)
        self._notes.append(note)
        print("Note was added.")

    def _edit_note(self) -> None:
        print("Which note would you like to edit?")
        self._show_notes()

        try:
            """
            Here it's quite important because we're going to ask them which note they want to edit.
            It's going to be equal to the integer value of the input that asks them for the index.
            Even if our list is going to start with the index of zero, we want it to start with the index of 1 so we do - 1.
            """

            note_index: int = int(input("Index: ")) - 1

            """
            That's how we're going to grab that note we want to edit.
            """

            current_note: Note = self._notes[note_index]
            new_title: str = input("New title: ")
            new_body: str = input("New body: ")
            current_note.title = new_title
            current_note.body = new_body
            print("Note was edited.")

            """
            It is important to remember that the first two lines of the try except, can possibly raise exceptions.
            One of them is the IndexError. Because they might select an index which does not exist.
            Another exception we might run into is a value error.
            The exception value error will cover everything that can possible go wrong when we're trying to convert the input to an integer (note_index)
            """

        except IndexError:
            print("Index out of range. Please try again with a valid index.")
            self._edit_note()
        except ValueError:
            print("Index cannot be empty.")
            print("Aborting operation...")
            self._edit_note()

    def _delete_note(self) -> None:
        print("Which note would you like to delete?")
        self._show_notes()

        try:
            note_index: int = int(input("Index: ")) - 1
            """
            Del = deleting the note we want to delete at the index we input.
            """
            del self._notes[note_index]
            print("Note was deleted.")
        except IndexError:
            print("Index out of range. Please try again with a valid index.")
            self._delete_note()
        except ValueError:
            print("Index cannot be empty.")
            print("Aborting operation...")
            self._delete_note()

    def _show_notes(self) -> None:
        """
        This will check if there are notes or not. And if there aren't any notes of course we want to print that here are no notes, and we will return no notes.
        """
        if not self._notes:
            print("There are no notes.")
        for i, note in enumerate(self._notes, start=1):
            print(f"{i}. {note.title}: {note.body}")

    def _select_option(self, user_input: str) -> None:
        if user_input not in {"1", "2", "3", "4", "5"}:
            print("Invalid input. Please try again with a valid option.")
            return

        if user_input == "1":
            self._add_note()
        elif user_input == "2":
            self._edit_note()
        elif user_input == "3":
            self._delete_note()
        elif user_input == "4":
            self._show_notes()
        elif user_input == "5":
            self.display_instructions()

    def run_app(self) -> None:
        while True:
            user_input: str = input("You: ")
            self._select_option(user_input)


def main() -> None:
    sample_notes: list[Note] = [Note(title="Title1", body="Hello there, Vincent!"),
                                Note(title="Title2", body="Hello there, John!"),
                                Note(title="Title3", body="Hello there, Vladimir!"),]
    note_app: NoteApp = NoteApp(author="Vincent", notes=sample_notes)
    note_app.run_app()


if __name__ == "__main__":
    main()
