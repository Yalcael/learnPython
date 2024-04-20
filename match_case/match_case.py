"""
Match case it's like the same as if else statements.
"""

# status: int = 200
#
# match status:
#     case 200:
#         print("Connected!")
#     case 403:
#         print("Forbidden")
#     case 404:
#         print("Not Found")
#     case _:
#         print("Unknown error")
while True:
    user_input: str = input("Enter a command: ")
    command: list = user_input.split()

    match command:
        case "find", *images:
            print(f"Finding: {images}...")
        case "enlarge", image, amount:
            print(f"Enlarge: {image} by {amount}x")
        case "rename", image, new_name if len(new_name) > 3:
            print(f"Rename: {image} to {new_name}")
        case "download", *images:
            print(f"Download: {images}...")
        case "x" | "delete", *images:
            print(f"Delete: {images}...")
        case _:
            print("Command not found")
