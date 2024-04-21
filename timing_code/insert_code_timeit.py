from timeit import timeit, repeat
# You can also choose to provide a setup using a multi-line string if that's what you want.
setup: str = """
import math

a: int = 10
b: int = 3
"""

math_power_time: float = timeit(stmt="math.pow(a, b)", setup=setup)
print(f"math.pow = {math_power_time:.3f}s")

power_time: float = timeit("a**b", setup="a, b = 10, 3")
print(f"a**b = {power_time:.3f}s")
