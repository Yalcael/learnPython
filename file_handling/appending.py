file_path: str = "info.txt"

with open(file_path, "a") as txt:
    # txt.write("Hello World!\n")
    txt.writelines(["Hello\n", "World\n", "Baguette\n"])

# While we are in append mode, that if you refer to a file path that doesn't exist, such as test.txt,
# Python is just going to create that file for us with the data we specified.
