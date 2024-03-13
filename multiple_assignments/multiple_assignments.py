def multiple_assignments():
    a = b = c = d = []
    print(a, b, c, d)
    print(a is b)  # True
    #   These are in fact all just different names for the same copy of the empty list.
    tmp = []
    a = tmp
    b = tmp
    c = tmp
    d = tmp

    # a, b = [], []
    # print(a is b)   # False


def tricky_multiple_assignments():
    a, b = a[:] = [[]], []
    print(a, b)

    tmp = [[]], []
    a, b = tmp  # a is equal to [[]], and b is equal to []
    a[:] = (
        tmp  # Assigns the contents of a equal to the right hand side, so the content of a will become equal to the contents of this tuple. So a will contain [[]], [].
    )
    print(a is a[0])  # a is equal to [...]
    #   You first evaluate the right hand side and the ngo left to right assigning things in turn.


def multiple_assignments_expressions():
    (
        a := (b := (c := (d := 0)))
    )  # d := 0 is going to return that zero back to me, which i then assign to c and then to b and then to a.
    print(a, b, c, d)
    # You're not allowed to chain multiple assignment expressions together unless you put them in parentheses.


if __name__ == "__main__":
    multiple_assignments()
    tricky_multiple_assignments()
    multiple_assignments_expressions()
