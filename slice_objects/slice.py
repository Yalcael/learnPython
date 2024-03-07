numbers: list[int] = list(range(1, 11))
text: str = "Hello World!"

rev: slice = slice(None, None, -1)
f_five: slice = slice(None, 5)

print(numbers[rev])
print(text[rev])
