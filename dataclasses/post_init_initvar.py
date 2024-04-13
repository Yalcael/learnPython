from dataclasses import dataclass, field, InitVar


@dataclass
class Fruit:
    name: str
    grams: float
    cost_per_kg: float
    is_rare: InitVar[bool | None] = None
    total_price: float = field(init=False)

    def __post_init__(self, is_rare: bool | None) -> None:
        if is_rare:
            self.cost_per_kg *= 2
        self.total_price = (self.grams / 1000) * self.cost_per_kg

    def describe(self) -> None:
        print(f"{self.grams}g of {self.name} costs {self.total_price}$")


def main() -> None:
    apple: Fruit = Fruit("Apple", 1500, 4)
    orange: Fruit = Fruit("Orange", 2500, 8)
    passion: Fruit = Fruit("Passion", 100, 50, is_rare=True)
    print(apple)
    print(orange)
    print(passion)
    apple.describe()
    orange.describe()
    passion.describe()


if __name__ == '__main__':
    main()
