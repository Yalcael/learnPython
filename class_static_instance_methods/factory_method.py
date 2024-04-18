from typing import Self


class Car:
    LIMITER: int = 200

    def __init__(self, brand: str, max_speed: int) -> None:
        self.brand: str = brand
        self.max_speed: int = max_speed

    @classmethod
    # Class method affect the actual class and not the instance.
    def change_limit(cls, new_limit: int) -> None:
        cls.LIMITER = new_limit

    @classmethod
    def autogenerate_max_speed(cls, brand: str) -> Self:
        lowered: str = brand.lower()
        max_speed: int = 200

        if lowered == "toyota":
            max_speed = 270
        elif lowered == "bmw":
            max_speed = 280
        elif lowered == "volvo":
            max_speed = 300

        return cls(brand, max_speed)

    def display_info(self) -> None:
        print(f'Brand: {self.brand}')
        print(f'Max speed: {self.max_speed}, limiter={self.LIMITER}')


def main() -> None:
    volvo: Car = Car.autogenerate_max_speed("Volvo")
    some_car: Car = Car.autogenerate_max_speed("Ferrari")
    bmw: Car = Car.autogenerate_max_speed("BMW")
    volvo.display_info()
    some_car.display_info()
    bmw.display_info()


if __name__ == '__main__':
    main()
