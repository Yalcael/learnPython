# keyword argument = an argument preceded by an identifier
# helps with readability
# Order of arguments doesn't matter
# 1: Positional, 2: Default, 3: KEYWORD, 4: Arbitrary
# def hello(greeting, title, first, last):
# print(f'{greeting} {title} {first} {last}')


# hello('Hello', title='World', first='Vincent', last='Lemaire')
# for x in range(1, 11):
# print(x, end=" ")

# print('1', '2', '3', '4', '5', sep='-')


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"


phone_number = get_phone(country=336, area=9322, first=20, last=69)
print(phone_number)
