class Car:
    LIMITER: int = 200

    def __init__(self, brand: str, max_speed: int) -> None:
        self.brand: str = brand
        self.max_speed: int = max_speed
        # self.LIMITER = 10

    @classmethod
    # Class method affect the actual class and not the instance.
    def change_limit(cls, new_limit: int) -> None:
        cls.LIMITER = new_limit
    # If we did self.LIMITER, it won't refer to the CONSTANT LIMITER. It would create a new instance attribute that would only belong to the current instance.
    # So if we create a Toyota and we update self.LIMITER, with a value of 150, only the Toyota is going to be updated not the rest of the Cars.
    # While with a cls method, this will update all the Cars. Because we are referencing to the Class LIMITER, not the instance LIMITER.

    def display_info(self) -> None:
        print(f'Brand: {self.brand}')
        print(f'Max speed: {self.max_speed}, limiter={self.LIMITER}')
        # Here self.LIMITER refer to the constant LIMITER because it's the only one it can find in the class.
        # But if we create a self.LIMITER = 10 as an instance, this one will default take the one we create.
        # Just remember that if we don't define the self.LIMITER inside our class as an instance attribute, it's going to use the one that's define as a Class Attribute.


def main() -> None:
    bmw: Car = Car('BMW', 240)
    toyota: Car = Car('Toyota', 190)

    bmw.display_info()
    toyota.display_info()
    Car.change_limit(150)
    bmw.display_info()
    toyota.display_info()
    # The class method affects all the instances regardless from where you called it.
    """
    If we do toyota.LIMITER for example, and set it to 140, so toyota.LIMITER = 140, in this case we're creating a new instance Attribute called LIMITER.
    But only for toyota. So if you run it, it's only going to change the LIMITER of the toyota.
    It's no longer using the class attribute, it's now using an instance attribute.
    """


if __name__ == '__main__':
    main()
