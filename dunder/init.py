# __init__ -> is a special method in Python, it is automatically called when you create an instance of a class.
# It's primary purpose is to initialize the attributes or properties of an object during object creation.
# It is also know as initializer or constructor method.

class MyClass:
  def __init__(self, arg1, arg2, ...):
    # Initialization code here
# The self parameter refers to the instance of the object  being created, and you can pass any other arguments you need.
    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    # Creating an instance of the Dog class
    my_dog = Dog('Buddy', 3)

    # When we create an instance of the dog class, the init method is automatically called,
    # it takes the parameter, name and age and assigns them as attributes to the object my_dog.
    # This way we can initialize the object with specific values.
    # You can use it to set default values, perform setup takes or validate input data when creating objects.
    # It's also a great place to define instant specific attributes.
