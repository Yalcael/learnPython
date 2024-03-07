class Calculator:
    def __init__(self, version: int) -> None:
        self.version = version

    def description(self):
        print(f"Version: {self.version}")  # Instance method

    @staticmethod
    def add_numbers(*numbers: float) -> float:  # Static Method
        return sum(numbers)


if __name__ == "__main__":
    calc1 = Calculator(200)
    calc2 = Calculator(300)
    calc3 = Calculator(500)
    # Instance Method

    calc1.description()
    calc2.description()
    calc3.description()
    # Instance Method

    print(Calculator.add_numbers(10, 30, 40))
    # Static Method


# Instance method,
# It is referring to self which refers to this instance over there,
# Which means if we create a new instance from this calculator we're going to be able to use that version from the instance not from the class.
# We can directly modify this instance thanks to the self keyword.

# Static method, is just a method that can be used anywhere that doesn't rely on the class,
# So add_numbers can effectively be outside of this class, and it won't affect anything because we do not use the instance inside this function.
# @staticmethod can be placed anywhere inside your program, and it won't affect the class, and it will still run properly.
# But a general reason you'll keep a static method inside a class is because it pairs nicely with the class that you are working with.
