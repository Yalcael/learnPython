import random
import sys

# Step 1 : Starting information
print("------------------------------------")
print("Welcome to Rock, Paper, Scissors Game!")
print("------------------------------------")

moves = {"Rock": "🪨", "Paper": "📃", "Scissors": "✂️"}
valid_moves = list(moves.keys())
user_point = 0
computer_point = 0

# Step 2 : Infinite Loop
while True:
    user_move: str = input("Choose : Rock, Paper, Scissors: ")
    if user_move == "exit":
        print("Thanks for playing!")
        sys.exit()

    if user_move not in valid_moves:
        print("------------------------------------")
        print("Invalid move, please try again using Rock, Paper or Scissors.")
        print("------------------------------------")
        continue

    # AI
    computer_move: str = random.choice(valid_moves)
    print("------------------------------------")
    print(f"You: {moves[user_move]}")
    print(f"Computer: {moves[computer_move]}")
    print("------------------------------------")

    # Check moves
    if user_move == computer_move:
        print("It's a tie!")
    elif user_move == "Rock" and computer_move == "Scissors":
        print("You win!")
        user_point += 1
        print("------------------------------------")
        print(f" Live score : You : {user_point} vs Computer : {computer_point}")
        print("------------------------------------")
    elif user_move == "Scissors" and computer_move == "Paper":
        print("You win!")
        user_point += 1
        print("------------------------------------")
        print(f" Live score : You : {user_point} vs Computer : {computer_point}")
        print("------------------------------------")
    elif user_move == "Paper" and computer_move == "Rock":
        print("You win!")
        user_point += 1
        print("------------------------------------")
        print(f" Live score : You : {user_point} vs Computer : {computer_point}")
        print("------------------------------------")
    else:
        print("Computer win!")
        computer_point += 1
        print("------------------------------------")
        print(f" Live score : Computer : {computer_point} vs You : {user_point}")
        print("------------------------------------")

    # Define a winner
    if user_point == 5:
        print("------------------------------------")
        print("You win the series! YOU ARE THE GOAT")
        print("------------------------------------")
    elif computer_point == 5:
        print("------------------------------------")
        print("Computer win the series! Better luck next time.")
        print("------------------------------------")
    else:
        print("The game is still going, first to win 5 rounds!")
