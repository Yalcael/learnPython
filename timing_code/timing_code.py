"""One of the major reasons to time your code is to see if you can optimize .
Because when you are writing code for the first time, you're not always going to pick the best approach,
which means there's going to be a lot of room for improvement and timing your code can be a great way to see if any of the changes actually improved the performance.
To time code in Python, we're going to be using a built-in module called Time it."""

# Warm up = Make sure that the interpreter is performing at peak performance. It just helps us get back more consistent and unbiased results.
# Repeat function is probably the safest way to get back consistent and unbiased results when you are using the timeit module.

from timeit import timeit, repeat


a: str = "list(range(1000))"
b: str = "list(range(1000))"
c: str = "set(range(1000))"

a_time: float = min(repeat(stmt=a, repeat=5, number=100000))
b_time: float = min(repeat(stmt=b, repeat=5, number=100000))
c_time: float = min(repeat(stmt=c, repeat=5, number=100000))

print(f"a_time: {a_time:.3f}s")
print(f"b_time: {b_time:.3f}s")
print(f"c_time: {c_time:.3f}s")


# warmup: float = timeit(stmt=a, number=100000)
# a_time: float = timeit(stmt=a, number=100000)
# b_time: float = timeit(stmt=b, number=100000)
#
# print(f"a_time: {a_time:.3f}s")
# print(f"b_time: {b_time:.3f}s")
