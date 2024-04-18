from typing import Callable


def use_all(f: Callable, values: list) -> None:
    for value in values:
        f(value)


use_all(lambda v: print(f"{v * "X"}"), [2, 4, 10])

# def multiply_x(value: int) -> None:
#     print(f"{value * "X"}")
# use_all(multiply_x, [2, 4, 10]
# This is the same as using the lambda function just above.


names: list = ["Bob", "John", "Smith"]
sorted_names: list = sorted(names, key=lambda x: len(x))
print(sorted_names)
