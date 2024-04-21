file_path: str = "info.txt"

with open(file_path, "r") as file:
    # print(file.read(5))
    # print(file.read(5))
    # print(file.read())
    # This is very useful if you are loading large files
    print(file.readline(5), end="")
    print(file.readline(3), end="")
    print(file.readline(), end="")   # This will read the rest of the line.
    print(file.readline(), end="")  # This is going to print the other line.
