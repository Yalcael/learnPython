import sys


def welcome_message() -> None:
    print("Welcome to the Vincent's Grocery!")
    print("Enter: ")
    print("------------------------------------")
    print("1. Add a grocery")
    print("2. Remove a grocery")
    print("3. Display")
    print("0. Exit")
    print("------------------------------------")


def add_tem(item: str, groceries: list[str]) -> None:
    groceries.append(item)
    print(f"'{item}' has been added!")


def remove_item(item: str, groceries: list[str]) -> None:
    try:
        groceries.remove(item)
        print(f"'{item}' has been removed!")
    except ValueError:
        print(f"'{item}' is not in the groceries!")


def display_groceries(groceries: list[str]) -> None:
    print("-------------LIST-------------------")
    for i, item in enumerate(groceries, 1):
        print(f"{i}: {item.capitalize()}")
    print("------------------------------------")


def is_an_option(text: str) -> bool:
    return text in ["1", "2", "3", "0"]


def main() -> None:
    groceries: list[str] = []

    welcome_message()
    while True:
        user_input: str = input("Choose: ").lower()

        if not is_an_option(user_input):
            print("Invalid. Please pick a valid option...")
            continue

        if user_input == "1":
            new_item: str = input("What item would like to add?: ").lower()
            add_tem(new_item, groceries)
        elif user_input == "2":
            item_to_remove: str = input("What item would you like to remove?: ").lower()
            remove_item(item_to_remove, groceries)
        elif user_input == "3":
            display_groceries(groceries)
        elif user_input == "0":
            print("Thank you for coming to the Vincent's Grocery!")
            sys.exit()


if __name__ == "__main__":
    main()
