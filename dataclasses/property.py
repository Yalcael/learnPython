from dataclasses import dataclass


@dataclass
class Fruit:
    name: str
    grams: float
    cost_per_kg: float

    @property
    def total_cost(self) -> float:
        return (self.grams / 1000) * self.cost_per_kg

    def describe(self) -> None:
        print(f"{self.grams}g of {self.name} costs {self.total_cost}$")


def main() -> None:
    apple: Fruit = Fruit("Apple", 1500, 4)
    print(apple)
    apple.describe()
    apple.cost_per_kg = 20
    print(apple)
    apple.describe()


if __name__ == '__main__':
    main()
