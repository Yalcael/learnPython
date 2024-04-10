# python program to demonstrate merging of lists using python
def append_lists():
    # list 1
    ls1 = [1, 2, 3, 4]
    # list 2
    ls2 = [5, 6, 7, 8]

    # iterating over list2
    for i in ls2:
        # appending in list1
        ls1.append(i)
    print(ls1)


# function call
append_lists()


# merge lists Using the '+' operator
def merge():
    # list 1
    ls1 = [15, 20, 35, 40]
    # list 2
    ls2 = [99, 44, 13]
    # merging using '+' operator
    ls = ls1 + ls2
    print(ls)


# function call
merge()


def list_comprehension():
    num1 = [1,2,3]
    num2 = [4,5,6]
    # using list comprehension
    num3 = [x for n in (num1, num2) for x in n]
    print(num3)


# function call
list_comprehension()


def extend_lists():
    # list 1
    ls1 = [11,19,25,40]
    # list 2
    ls2 = [31,84,13]
    ls1.extend(ls2)
    print(ls1)


# function call
extend_lists()
