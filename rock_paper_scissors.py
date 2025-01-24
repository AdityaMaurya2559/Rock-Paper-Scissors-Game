import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

def display_score(player_score, computer_score):
    print("\n--- Scoreboard ---")
    print(f"Player: {player_score} | Computer: {computer_score}")
    print("------------------")

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit.")
    
    player_score = 0
    computer_score = 0
    
    while True:
        player_choice = input("\nYour choice (rock/paper/scissors): ").lower()
        if player_choice == "exit":
            print("\nThanks for playing! Final scores:")
            display_score(player_score, computer_score)
            break

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        if result == "player":
            print("You win this round!")
            player_score += 1
        elif result == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a draw!")

        display_score(player_score, computer_score)

# Start the game
play_game()
