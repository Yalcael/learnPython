from typing import Self
from datetime import date


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def description(self) -> str:
        return f"{self.name} is {self.age} years old"

    @classmethod
    def age_from_year(cls, name: str, birth_year: int) -> Self:
        current_year: int = date.today().year
        age: int = current_year - birth_year
        return cls(name, age)


if __name__ == "__main__":
    vincent = Person.age_from_year("Vincent", 1999)
    print(vincent.description())

# You notice something funky there, that we have CLS instead of self, and that's because we are now editing the class directly.


# Class method, is going to affect the actual class while.
