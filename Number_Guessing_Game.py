import random

print("=== Number Guessing Game ===")
print("I'm thinking of a number between 1 and 50.")
print("You have 3 attempts to guess it. Good luck!\n")

number = random.randint(1, 50)
attempts = 3
guess = None

while attempts > 0:
    user_input = input(f"Guess the number (Attempts left: {attempts}): ")

    if not user_input.isdigit():
        print("Oops! Please enter a valid number.")
        continue
    
    guess = int(user_input)

    if guess == number:
        print(f"Yay! You guessed it right. The number was {number}. ")
        break
    elif guess < number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

    attempts -= 1

if attempts == 0 and guess != number:
    print(f"Game over! The number I picked was {number}. Better luck next time! ")
