# Exception classes
# Raise = To raise an error
# Try = which tries to execute code in a block
# except = that allows to handle particular types of exceptions
# finally = which is code that is run after the try block in all cases, whether there's an exception or not.


def process(data: str) -> None:
    print("Processing data")


def main() -> None:
    file = None
    try:
        file = open("data.txt", "r")
        data = file.read()
    except IOError:
        print("Error reading file")
    else:
        #   Process the data
        process(data)
    finally:
        if file is not None:
            file.close()
