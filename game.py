"""Mystery Number Challenge - a beginner-friendly Python guessing game."""

import random


LOWEST_NUMBER = 1
HIGHEST_NUMBER = 100
MAX_ATTEMPTS = 5


def get_guess():
    """Ask for a whole-number guess and keep asking until input is valid."""
    while True:
        user_input = input(
            f"Enter a number between {LOWEST_NUMBER} and {HIGHEST_NUMBER}: "
        ).strip()

        try:
            guess = int(user_input)
        except ValueError:
            print("Please enter a whole number, such as 42.")
            continue

        if not LOWEST_NUMBER <= guess <= HIGHEST_NUMBER:
            print(
                f"Your number must be between {LOWEST_NUMBER} "
                f"and {HIGHEST_NUMBER}."
            )
            continue

        return guess


def play_round():
    """Play one round of the game."""
    secret_number = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)

    print("\n" + "=" * 38)
    print("       MYSTERY NUMBER CHALLENGE")
    print("=" * 38)
    print(f"I'm thinking of a number from {LOWEST_NUMBER} to {HIGHEST_NUMBER}.")
    print(f"You have {MAX_ATTEMPTS} attempts to guess it. Good luck!")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        print(f"\nAttempt {attempt} of {MAX_ATTEMPTS}")
        guess = get_guess()

        if guess == secret_number:
            print(f"Correct! 🎉 The mystery number was {secret_number}.")
            print(f"You guessed it in {attempt} attempt(s)!")
            return

        if guess < secret_number:
            print("Too low! Try a higher number. 🔼")
        else:
            print("Too high! Try a lower number. 🔽")

        attempts_left = MAX_ATTEMPTS - attempt
        if attempts_left:
            print(f"You have {attempts_left} attempt(s) left.")

    print(f"\nGame over! The mystery number was {secret_number}. Better luck next time!")


def main():
    """Run rounds until the player chooses to stop."""
    print("Welcome to Mystery Number Challenge!")

    while True:
        play_round()
        play_again = input("\nWould you like to play again? (y/n): ").strip().lower()

        if play_again not in ("y", "yes"):
            print("\nThanks for playing. See you next time! 👋")
            break


if __name__ == "__main__":
    main()
