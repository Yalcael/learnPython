import time
from typing import Callable
from functools import wraps


def get_time(func: Callable) -> Callable:
    """Times how long it takes to run the function"""

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        start: float = time.perf_counter()
        func(*args, **kwargs)
        end: float = time.perf_counter()
        print(f"Time: {end - start:.3f}s")
    return wrapper


@get_time
def calculate() -> None:
    """Calculate() docstring"""

    print("Calculating...")
    # for i in range(10000000):
    #     pass
    time.sleep(2)

    print("DONE")


def main() -> None:
    print(calculate.__name__)
    print(calculate.__doc__)


if __name__ == '__main__':
    main()
