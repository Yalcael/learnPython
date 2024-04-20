from typing import Callable, Any
from functools import wraps


def repeat(number: int) -> Callable:
    """Repeat a function call x amount of times."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any | None:
            value: Any = None
            for _ in range(number):
                value = func(*args, **kwargs)
            return value

        return wrapper
    return decorator


@repeat(2)
def greet(name: str) -> None:
    """A function used to greet the user."""
    print(f"Hello {name}!")


@repeat(2)
def add(a: int, b: int) -> int:
    """A function used to add two numbers together."""
    print(f"{a+b=}")
    return a + b


def main() -> None:
    result: int = add(4, 3)
    greet("Vincent")
    print(result)


if __name__ == '__main__':
    main()
