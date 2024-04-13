from dataclasses import dataclass, field


@dataclass
class Fruit:
    name: str
    grams: float
    cost_per_kg: float
    total_price: float = field(init=False)

    def __post_init__(self) -> None:
        self.total_price = (self.grams / 1000) * self.cost_per_kg

    def describe(self) -> None:
        print(f"{self.grams}g of {self.name} costs {self.total_price}$")


def main() -> None:
    apple: Fruit = Fruit("Apple", 1500, 4)
    orange: Fruit = Fruit("Orange", 2500, 8)
    print(apple)
    print(orange)
    apple.describe()
    orange.describe()


if __name__ == '__main__':
    main()
