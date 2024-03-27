def swap(data, a, b):
    temp = data[a]  # Temporary variable, to store one of the two items
    data[a] = data[b]  # then put the other item in its place
    data[b] = (
        temp  # And then put the temporary one that we store beforehand in the other place
    )


# It's a three-line function that swaps two items in place on the same list.
# The reason why we need this temporary variable because one of the items will get overwritten in the middle of the swap.
# So we had to make a backup of that beforehand


data = [6, 5, 4, 3, 2, 1]
for i in range(
    1, len(data)
):  # First loop, we use a range here because A RANGE represents a sequence of numbers. It starts at 1 and stop at len(data).
    for j in range(1, len(data)):  # Second Loop
        if data[j] < data[j - 1]:  # Basically, we're comparing two adjacent items.
            swap(
                data, j, j - 1
            )  # If the one behind is smaller, then we swap them, this is the basic logic of bubble sort.
            # It just loops through the data many times and each time it only focuses on two adjacent items.

print(data)
