from typing import Self


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"{self.name} is {self.age} years"

    def __lt__(self, other: Self) -> bool:
        print("Using: __lt__")
        return self.age < other.age

    def __gt__(self, other: Self) -> bool:
        print("Using: __gt__")
        return self.age > other.age

    def __eq__(self, other: Self) -> bool:
        print("Using: __eq__")
        return self.age == other.age


def main() -> None:
    people: list[Person] = [
        Person("John", 20),
        Person("James", 30),
        Person("Smith", 22),
        Person("Bob", 28),
    ]
    # people.sort()
    # print(sorted(people))
    # print(people[0] < people[1])
    # print(people[0] > people[1])
    print(people[0] == people[1])


if __name__ == "__main__":
    main()
