# name = input('Enter your full name: ')
# phone_number = input('Enter your phone number: ')

# result = len(name) Length of the name
# result = name.find("V"), First occurrence
# result = name.rfind("V"), Last occurrence
# name: str = name.capitalize(), Capitalize the first letter
# name: str = name.upper(), Makes all the letters uppercase
# name: str = name.lower(), Males all the letters lowercase
# result: bool = name.isdigit(), Return true if it contains digits, else false
# result: bool = name.isalpha(), Return true if it contains only letters, else false
# result: int = phone_number.count('-')
# phone_number: str = phone_number.replace('-', ' ')

# print(phone_number)
# print(help(str))

username = input("Enter a username: ")


if len(username) > 12:
    print("Your username can not be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can not contain spaces")
elif not username.isalpha():
    print("Your username can not contain numbers")
else:
    print(f"Welcome: {username}")
