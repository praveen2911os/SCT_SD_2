import random


def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess_text = input("Enter your guess: ")
        try:
            guess = int(guess_text)
        except ValueError:
            print("Please enter a valid integer between 1 and 100.")
            continue

        if guess < 1 or guess > 100:
            print("Please guess a number within the range 1 to 100.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low. Try again.")
        elif guess > number_to_guess:
            print("Too high. Try again.")
        else:
            print(f"Correct! The number was {number_to_guess}.")
            print(f"You guessed it in {attempts} attempt{'s' if attempts != 1 else ''}.")
            break


def main():
    while True:
        play_game()
        again = input("Would you like to play again? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
