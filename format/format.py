from typing import Any


class Book:
    def __init__(self, title: str, pages: int) -> None:
        self.title = title
        self.pages = pages

    def __format__(self, format_spec: Any) -> str:
        match format_spec:
            case "time":
                return f"{self.pages / 60:.2f}h"
            case "caps":
                return self.title.upper()
            case _:
                raise ValueError(f"Unknown specifier for Book()")


def main() -> None:
    harry_potter: Book = Book("Harry Potter", 300)

    print(f"{harry_potter:caps}")
    print(f"Read time: {harry_potter:time}")


if __name__ == "__main__":
    main()
