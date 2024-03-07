set_a: set[int] = {1, 2, 3, 4, 5}
set_b: set[int] = {4, 5, 6, 7, 8}

print(set_a | set_b)
# This will combine the 2 sets

print(set_a - set_b)
# This will subtract elements

print(set_a & set_b)
# This operation is going to give us back all the elements that are share.
# In other words, the intersection of this 2 sets.

print(set_a ^ set_b)
# This will give us only the unique elements, also known as the symetrics difference.
