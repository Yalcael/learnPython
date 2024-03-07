from collections import namedtuple


def init_count():
    count = 0  # Variable

    def add(
        amount,
    ):  # Inner function, the add function will add the amount parameter to the count variable
        nonlocal count
        count += amount

    def get_count():
        return count

    Count = namedtuple("Count", ["add", "get_count"])
    return Count(add, get_count)


# Once we return the function add, the count variable will be capture and save in a closure
# And then it can still be access through calling this function from the outside world.


count = init_count()
count.add(1)
count.add(1)
print(count.get_count())  # The result will be 2.

new_add, new_get_count = init_count()
# It's like creating a new object instance from a class,
# the count variable is like a private attribute that can only be accessed through these two functions.

# 'Closure'
#
# 'Closure is the programming technique of returning an inner function from an outer function.
# It allows you to capture the variable from the outer function, and use them again even after the function has been exited.'
