from typing import Generator


def huge_data() -> Generator:
    for i in range(1, 100000000000):
        yield i


def generate_vowels() -> Generator:
    vowels: str = "aeiouAEIOU"
    for vowel in vowels:
        yield vowel


def main() -> None:
    data: Generator = huge_data()
    for i in range(200):
        print(next(data))
    vowels: Generator = generate_vowels()
    for vowel in vowels:
        print(vowel)


if __name__ == '__main__':
    main()
