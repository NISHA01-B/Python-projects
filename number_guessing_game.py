import random

def number_guessing_game():
    """
    A simple number guessing game.
    The program generates a random number, and the user has to guess it.
    Feedback is provided to indicate if the guess is too high or too low.
    """

    # Set the range for the random number
    lower_limit = 1
    upper_limit = 100

    # Generate a random number between the specified range
    secret_number = random.randint(lower_limit, upper_limit)

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_limit} and {upper_limit}. Can you guess what it is?")

    # Initialize the variable to store the user's guess
    user_guess = None

    # Continue looping until the user guesses the correct number
    while user_guess != secret_number:
        try:
            # Ask the user for their guess
            user_guess = int(input("Enter your guess: "))

            # Check if the guess is too high, too low, or correct
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it right. The number was {secret_number}. 🎉")
        except ValueError:
            print("Please enter a valid number.")

# Start the game
number_guessing_game()
