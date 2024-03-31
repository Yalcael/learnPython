import string


def is_letters_only(text: str) -> None:
    alphabet: str = string.ascii_letters + "," + "-" + " "

    for char in text:
        if char not in alphabet:
            raise ValueError("Text can only contain letters from the alphabet.")
    print(f"{text} is letters-only. Noice!")


def main() -> None:
    while True:
        try:
            user_input: str = input("Check text: ")
            is_letters_only(user_input)
        except ValueError:
            print("Please only enter English letters.")
        except Exception as e:
            print(f"An unknown error occurred: {type(e)} {e}")


main()
