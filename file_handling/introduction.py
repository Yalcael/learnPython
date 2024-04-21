from typing import TextIO
# RAW = Read / Append and Write

file_path: str = "info.txt"

# Classic way to open and read a file :
# file: TextIO = open(file_path, "r")     # "r" = read mode
# text: str = file.read()
# print(text)
# file.close()
"--------------------------------------------"

# with open(file_path, "r") as f:
#     print(f.read())

# The with block will automatically close the file as soon as we exit this with block, which means...
# Even if there's an exception or something goes wrong, file.close will always be called.
"--------------------------------------------"

try:
    with open(file_path, "r") as f:
        text: str = f.read()

    print(text)
except FileNotFoundError:
    print(f"{file_path} is not found.")
