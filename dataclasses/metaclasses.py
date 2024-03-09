class MyMetaclass(type):
    pass


class A(metaclass=MyMetaclass):
    pass


def main():
    a = A()
    print(f"{type(a)=}")
    print(f"{type(A)=}")


if __name__ == "__main__":
    main()

# A metaclass is just the type of a type or the class of a class
