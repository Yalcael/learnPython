# Indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step]

credit_card = "1234-5678-1234-4564"
# print(credit_card[0])     # First character of a string
# print(credit_card[:4])    # From the start until index 4
# print(credit_card[5:9])
# print(credit_card[5:])    # index 5 till the end of the string
# print(credit_card[-1])  # Last character of a string
# print(credit_card[::2])   # from beginning till the end, have a step of 2
last_digit: str = credit_card[-4:]
print(f"The last digit of the credit card: {last_digit}")

credit_card: str = credit_card[::-1]
print(credit_card)
# Reverse a string
