fruits = ["apple", "banana", "orange", "grape", "kiwi", "lemon", "watermelon"]
print(fruits[3])
print(fruits[0:3])
print(fruits[1:3])
print(fruits[:3])
print(fruits[1:])
print(fruits[1:] + fruits[:1])
print(fruits[-3:])
print(fruits[:-3])
print(fruits[::1])
print(fruits[::2])
print(fruits[::3])
print(fruits[::-1])
print(list(reversed(fruits)))

# Slicing makes a new list,
# The start of index is inclusive but the stop index is exclusive,
# Slicing works on all sequences,
