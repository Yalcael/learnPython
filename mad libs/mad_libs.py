name: str = input("Enter a name: ")
noun_a: str = input("Enter a noun: ")
verb_a: str = input("Enter a verb: ")
noun_b: str = input("Enter a noun: ")
verb_b: str = input("Enter a verb: ")
number: str = input("Enter a number: ")

story: str = f"""
-----------------------------------------------------------------
This is a beautiful story about {name}, a strong and wonderful {noun_a} who loved to {verb_a}.

{name} once {verb_b} a game and won a {noun_b} as a prize. 
Isn't that incredible?

Today, {name} is {int(number)} years old and has retired from all adventures.

But the story will live on forever...
-----------------------------------------------------------------
"""
print(story)
