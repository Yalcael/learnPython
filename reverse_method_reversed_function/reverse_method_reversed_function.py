original_list = [1, 2, 3, 4, 5]
original_list.reverse()
print(original_list)

# Imagine we have a list of numbers that we want to reverse. Now when we use the reverse method on the original_list.
# In this case, the reverse() method is called directly on the original_list.
# The reverse() method modifies in the list in place, meaning it changes the order of elements directly within the existing list.
# After the reverse operation the original_list is updated and if you print it, you'll see the elements in original_list are reversed.

# Let's look at what happens when the function is reversed().
original_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(original_list))
print(reversed_list)

# In this case, the reversed() function is applied to the original_list.
# The reversed() function returns a reversed iterator but it does not modify the original list,
# to get a reversed list, we convert the reversed iterator to a list using the list function.
# So the original_list remains unchanged.
# And if you print both, you'll see the original_list retains its original order and the reversed elements are stored in the reversed_list.


# The reverse() method and the reversed() function
# The reverse() method is used to reverse the order of elements in a list in-place, meaning it modifies the original list.
#
# The reversed() is a built-in function that returns a reversed iterator of the given iterable, without modifying the original sequence.
# The reverse() method is a member of the list class, so it can only be used with lists. It doesn't return anything, instead, it reverses the list in place.
#
# The reverse() function is a built-in function that can be applied to any iterable, not just lists.
# It returns a reversed iterator, which can be converted back to a list or used in a loop.
