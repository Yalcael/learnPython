def description(numbers: list) -> dict:
    # numbers_length: int = len(numbers)
    # numbers_sum: int = sum(numbers)
    # numbers_mean: float = numbers_sum / numbers_length

    # The walrus operator does is both create the variable and return the result of this expression on the same line.

    details: dict = {"length": (numbers_length := len(numbers)),
                     "sum": (numbers_sum := sum(numbers)),
                     "mean": numbers_sum / numbers_length}
    return details


def main() -> None:
    numbers: list = [1, 27, 3, 54, 5555, 23, 7, 800, -9, 100]
    print(description(numbers))
    items: dict = {1: "Cup", 2: "Chair", 3: "Table"}
    # If we didn't want to use the walrus operator, we should have written = item: str | None = items.get(1)
    if item := items.get(2):
        print(f"You have: {item}")
    else:
        print("No item found...")


if __name__ == '__main__':
    main()
