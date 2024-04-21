import time
from functools import cached_property

"""cached_property is a decorator that converts a class method into a property whose value is calculated once and then cached like a regular attribute. 
The cached value will be available until the object or the instance of the class is destroyed."""
# cached_property will cache the data in a class.


class DataSet:
    def __init__(self, data: list) -> None:
        self._data = data

    def show_data(self) -> None:
        print(self._data)

    @cached_property
    def sum(self) -> float:
        print("Calculating sum...")
        time.sleep(2)
        return sum(self._data)

    @cached_property
    def mean(self) -> float:
        print("Calculating mean...")
        time.sleep(2)
        return sum(self._data) / len(self._data)


def main() -> None:
    ds: DataSet = DataSet([1.5, 2.5, 10, 15, 25.5])
    ds.show_data()

    while True:
        user_input: str = input("You: ").lower()

        if user_input == "clear sum":
            del ds.sum
            print("Cleared sum")
            # It's not actually going to delete the method, it's just going to delete the cache for the sum.
        elif user_input == "clear mean":
            del ds.mean
            print("Cleared mean")
            # It's not actually going to delete the method, it's just going to delete the cache for the mean.
        elif user_input == "sum":
            print(ds.sum)
        elif user_input == "mean":
            print(ds.mean)
        else:
            print("Unknown input...")


if __name__ == "__main__":
    main()
