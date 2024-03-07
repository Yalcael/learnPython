from typing import Callable


def multiply_setup(t: float) -> Callable:
    def multiply(b: float) -> float:
        return t * b

    return multiply


double: Callable = multiply_setup(2)
triple: Callable = multiply_setup(3)

print(double(5))
print(triple(5))
print(double(10))
print(triple(10))
