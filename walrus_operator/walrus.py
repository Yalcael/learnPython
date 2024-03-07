users: dict[int, str] = {0: "Bob", 1: "Alice", 2: "Dave"}

# user: str | None = users.get(1)

if user := users.get(0):
    print(f"{user} exists")
else:
    print("No user found...")


def get_info(text: str) -> dict:
    return {
        "words": (words := text.split()),
        "word_count": len(words),
        "character_count": len("".join(words)),
    }


print(get_info("Vincent"))
print(get_info("I love you"))
print(get_info("My name is Vincent Lemaire"))
