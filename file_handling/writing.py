file_path: str = "info.txt"

with open(file_path, "w") as txt:
    txt.write("Hello\n")
    txt.write("Vincent")

"""The big difference between appending and writing is that when we actually try to write something to this file,
it's going to wipe that whole file clean before performing the operation."""
