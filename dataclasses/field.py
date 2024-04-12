from dataclasses import dataclass, field


@dataclass
class Fruit:
    name: str
    grams: float
    price_per_kg: float
    edible: bool = field(default=True)
    related_fruits: list[str] = field(default_factory=list)


def main() -> None:
    apple: Fruit = Fruit('apple', 100.5, 5)
    orange: Fruit = Fruit('orange', 240, 5, edible=False, related_fruits=['apple', 'watermelon'])
    print(apple)
    print(orange)


if __name__ == '__main__':
    main()
