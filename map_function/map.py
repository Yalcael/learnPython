# Python map() function

# Have you ever wonder what you'd do if you wanted to apply a specific function to each item in an iterable without using a loop ?
# Particularly a for loop ? You can use the map() function to complete this task.

# The map() is a built-in Python function that takes a function and an iterable as arguments,
# applying that function to each item in the iterable and returning an iterator object containing the results.


# This iterator can be looped over or converted into a data type such as a list.
# Let me show you an example in which we have an add_two() function that takes an argument 'x' and increments it by 2 and an iterable named numbers.


def add_two(x):
    return x + 2


# function to be applied


numbers = [34, 23, 45, 10]
# list of integers


final_list = []
# emtpy list to store the final result


for item in numbers:
    result = add_two(item)
    final_list.append(result)

print(f"Final result: {final_list}.")
# using for loop

# In the first case you can see the add_two function is applied to each item in the iterable using the for loop.
# When you run this code you will se a list of original numbers that have been incremented by two.
# However, if you want the same task done in a concise and elegant manner, consider using the map() function.
# The map() can help you reduce iteration tasks and avoid writing unnecessary lines of code.


def add_two(x):
    return x + 2


numbers = [34, 23, 45, 10]
# list of integers


mapping = map(add_two, numbers)
result = list(mapping)
print(f"Final result: {result}.")
# Using map() function

# Check this out, when you run this code, it will produce the same result as the previous one.

# The map function isn't limited to just one iterable. You can actually pass multiple iterables and the function will be applied to the corresponding elements.


def add_numbers(x, y):
    return x + y


# Function to be applied


first_iterable = [2, 5, 9, 4]
second_iterable = [4, 8, 1, 7]
# Iterables


mapping = map(add_numbers, first_iterable, second_iterable)
result = list(mapping)
print(f"Final result: {result}.")
# Passing multiple iterables to map() function

# This time we are going to perform the sum operation on the corresponding values in both iterables
# You can see that we passed the add_numbers function and both iterables to the map() function, the output is the sum of the corresponding values from both iterables.
# So whether you're working with a single iterable or multiple ones, the map() function is a handy tool.
