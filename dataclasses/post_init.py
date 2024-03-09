from dataclasses import dataclass, field, InitVar


@dataclass
class Fruit:
    name: str
    grams: float
    cost_per_kg: float
    is_rare: InitVar[bool] = False
    similar_fruits: list[str] = field(default_factory=list)

    # Calculate later
    total_value: float = field(init=False)

    def __post_init__(self, is_rare: bool) -> None:
        self.total_value = (self.grams / 1000) * self.cost_per_kg

        if is_rare:
            self.total_value *= 2
            self.cost_per_kg *= 2


def main() -> None:
    apple: Fruit = Fruit("Apple", 2500, 3)
    banana: Fruit = Fruit("Banana", 1500, 10, is_rare=True)
    orange: Fruit = Fruit("Orange", 500, 1, similar_fruits=["Apple", "Lemon"])

    print(apple)
    print(banana)
    print(orange)


if __name__ == "__main__":
    main()
