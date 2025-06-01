import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to decide who wins
def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif user == 'rock':
        if computer == 'scissors':
            return "You win! Rock crushes scissors."
        else:
            return "You lose! Paper covers rock."
    elif user == 'paper':
        if computer == 'rock':
            return "You win! Paper covers rock."
        else:
            return "You lose! Scissors cut paper."
    elif user == 'scissors':
        if computer == 'paper':
            return "You win! Scissors cut paper."
        else:
            return "You lose! Rock crushes scissors."
    else:
        return "Invalid input. Please choose rock, paper or scissors."

# Main part of the game
print("=== Rock Paper Scissors Game ===")
print("Type 'rock', 'paper' or 'scissors' to play.")
print("Type 'exit' to quit the game.")

while True:
    user_choice = input("Your choice: ").lower()
    
    if user_choice == 'exit':
        print("Thanks for playing!")
        break

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = decide_winner(user_choice, computer_choice)
    print(result)
    print("-" * 30)
