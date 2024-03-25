print("Welcome to your simple adder!")
print('---------------------------------')

a: str = input("Enter your value for 'a': ")
b: str = input("Enter your value for 'b': ")
print('---------------------------------')

print("The result is:", int(a) + int(b))


number: list[int] = [1, 2, 3, 4]
print(number)
number.append(5)
print(number)
number.remove(5)
print(number)
number.pop(1)
print(number)
number.insert(1, 2)
print(number)
number[0] = 0
print(number)
