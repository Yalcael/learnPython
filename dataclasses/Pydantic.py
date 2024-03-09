def pydantic_example():
    from pydantic import BaseModel

    class T(BaseModel):
        n: int
        f: float
        s: str

    x = T(n=1, f=3.14, s="hello world")  # Must be kwargs
    y = x.n
    x.n = 0
    # args always converted to given types, type_checked at runtime.


# Pydantic is a very opinionated library built for doing a specific task: PARSING
# By default, Pydantic will try to convert things into these types when you construct this object or set an attribute, and it will check those types at runtime.
