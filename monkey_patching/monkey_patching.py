import time
import logging

"""What is Monkey Patching in Python? Imagine modifying a car's engine while it's running. 
Monkey patching works similarly, allowing you to dynamically alter or extend a class or module's behavior at runtime. 
It involves changing or adding methods or attributes to existing modules or classes."""


# class Internet:
#     def __init__(self, provider: str) -> None:
#         self.provider = provider
#
#     def connect(self) -> None:
#         print(f"Connecting to [{self.provider}]")
#         time.sleep(2)
#         print(f"Connected to [{self.provider}]")
#
#
# def test_connection() -> None:
#     print("[Provider] You are now connected")
def new_print(text: str) -> None:
    logging.warning(text)


def main() -> None:
    print = new_print
    print('Hello World!')
    print("Hi Vincent!")


if __name__ == '__main__':
    main()
