import sys


def welcome_message() -> None:
    print("Welcome to the Vincent's Grocery!")
    print("Enter: ")
    print("------------------------------------")
    print("1. Add a grocery")
    print("2. Remove a grocery")
    print("3. Display")
    print("4. Modify a grocery")
    print("0. Exit")
    print("------------------------------------")


def add_tem(item: str, groceries: list[str]) -> None:
    if item == "":
        print(f"Item {item} can't be added")
    elif item in groceries:
        print(f"Item {item} is already in the list")
    else:
        groceries.append(item)
        print(f"Item {item} has been added to the list!")


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
    return text in ["1", "2", "3", "4", "0"]


def modify_list_of_groceries(groceries: list[str]) -> None:
    print("Current list of groceries: ", groceries)
    item_to_modify = input("Enter the item you want to modify: ")
    if item_to_modify in groceries:
        new_item = input("Enter the new item: ")
        index = groceries.index(item_to_modify)
        groceries[index] = new_item
        print(f"'{item_to_modify}' has been modified to '{new_item}'.")
    else:
        print(f"'{item_to_modify}' is not in the list of groceries.")


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
        elif user_input == "4":
            modify_list_of_groceries(groceries)
        elif user_input == "0":
            print("Thank you for coming to the Vincent's Grocery!")
            sys.exit()


if __name__ == "__main__":
    main()
