import random

def guessing_game():
    """
    A number guessing game where the user guesses a random number between 1 and 100.
    Feedback is provided until the correct number is guessed.
    """
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")

    # Initialize user_guess as None
    user_guess = None

    # Continue until the correct number is guessed
    while user_guess != secret_number:
        try:
            # Prompt the user for a guess
            user_guess = int(input("Enter your guess: "))

            # Check if the guess is correct, too high, or too low
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number. It was {secret_number}! 🎉")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

# Run the game
guessing_game()
