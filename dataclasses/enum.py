from enum import Enum


class Colour(Enum):
    RED = 'R'
    GREEN = 'G'
    BLUE = 'B'
    YELLOW = 'Y'


def buy_car(brand: str, colour: Colour) -> None:
    if colour == Colour.RED:
        print(f'Brand: {brand} | Lovely red.')
    elif colour == Colour.GREEN:
        print(f'Brand: {brand} | Peaceful green.')
    elif colour == Colour.BLUE:
        print(f'Brand: {brand} | Dreamy blue.')
    elif colour == Colour.YELLOW:
        print(f'Brand: {brand} | Sunning yellow.')
    else:
        print("Unknown colour.")


def main() -> None:
    buy_car('Ferrari', Colour.RED)
    buy_car('Porsche', Colour.GREEN)
    buy_car('Fiat', Colour.BLUE)
    buy_car('BMW', Colour.YELLOW)
    buy_car('BMW', "Red")


if __name__ == '__main__':
    main()


"""
ENUM are a safe way of defining a fixed set of constant values that help drastically with reducing errors that we get from inputs.
Use enum if you know that there's a fixed set of options that a function can accept such as a lamp has an on and off state,
Or a car that only has a few colours to select."""
