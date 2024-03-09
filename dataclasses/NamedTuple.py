def namedtuple_example():
    from typing import NamedTuple

    class T(NamedTuple):
        n: int
        f: float
        s: str

    x = T(42, 4.5, "Hello World")
    x = T(42, f=4.5, s="Hello World")

    y = x[0]
    y = x.n

    # Immutable
    # This NamedTuple is a thin wrapper around the other one
    # It's still a tuple, and it still behaves exactly the same as the other one
    # The benefit though is that this way of defining the class, is much easier to read, and it also leaves a spaces for the type hints.
    # If you care about static typing at all, then you should always prefer this NamedTuple.
