import time
from functools import cache

"""Memoization is a method used to store the results of previous function calls to speed up future calculations. 
If repeated function calls are made with the same parameters, we can store the previous values instead of repeating unnecessary calculations. 
This results in a significant speed up in calculations."""


@cache
def count_vowels(text: str) -> int:
    print("Counting the number of vowels...")
    time.sleep(3)
    return sum(text.count(vowel)for vowel in 'AEIOUaeiou')


def main() -> None:
    while True:
        user_input: str = input("You: ").lower()

        if user_input == "info":
            print(f"Bot: {count_vowels.cache_info()}")
            # cache_info is going to return to us the info regarding the cache.
            # You can use this on any function that uses the cache decorator.
        elif user_input == "clear":
            count_vowels.cache_clear()
            print(f"Bot: Cache has been cleared!")
        else:
            print(f"Bot: That text contains {count_vowels(user_input)} vowels")


if __name__ == "__main__":
    main()
