# if __name__ == '__main__'
#
# A way to ensure that a specific block of code runs only when the Python script is executed directly. Not when it's imported as a module.
#
# __name__ -> is a built-in variable in Python. It represents the current module's name.
# When you run a Python script, Python assigns __main__ to the __name__ variable. If that script is the main program being executed.

# Imagine we have a Python script with the code flashing on the screen, in this code we define a function greet that prints a greeting
# and then we have the if __name__ == '__main__' block, this block will only run if you run the script directly, not if you import it into another Python file.


def greet(name):
    print(f'Hello, {name}!')


if __name__ == '__main__':
    user_name = input('Enter your name: ')
    greet(user_name)

# The benefit is all about making our code reusable by using if __name__ == '__main__'.
# It lets you create Python scripts that can be imported as modules into other scripts.
# When the script is imported as a module, the code inside the if __name__ == '__main__': block is not automatically executed.
from my_greet_module import greet


name = 'John Doe'
result = greet(name)
print(f'Welcome! {result}.')

# See, we imported our my_greet_module and use the greet functino without running the script's main code. This is fantastic for creating reusable code libraries.
# This can be especially handy in larger Python projects, where you have multiple scripts that work together.
# You can import functions and classes from one script into another without running the whole program every time.

