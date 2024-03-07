# for loop
squares = []
for num in range(1, 11):
    squares.append(num * num)

result = []
for num in range(1, 11):
    if num % 2 == 0:
        result.append("Even")
    else:
        result.append("Odd")

# list comprehension
squares = [num * num for num in range(1, 11)]
# [expression for item in iterable if condition]
# Expression: This is the operation or transformation that you want to perform on each item in the iterable.
# It could be anything from a simple arithmetic operation to a function call.
# Iterable: This is the collection of items over which you want to iterate. it can be a list, tuple, range or any other iterable object.
# Condition: Optional. This allows you to filter the items in the iterable based on a certain condition.

# Creating a list of squares of even numbers from 1 to 10
squares_of_evens = [num**2 for num in range(1, 11) if num % 2 == 0]

# if-else in list comprehension
result = ["Even" if num % 2 == 0 else "Odd" for num in range(1, 11)]


# List comprehension is a concise and powerful way to create lists in Python.
# It allows you to create a new list by applying an expression to each item in an existing iterable such as a list, tuple or range
# and optionally filtering the items based on a condition.
