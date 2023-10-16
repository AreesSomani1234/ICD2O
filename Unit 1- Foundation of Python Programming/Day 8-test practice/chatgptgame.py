import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess the secret number (between 1 and 100): "))
            attempts += 1

            if guess < secret_number:
                print("Try a higher number.")
            elif guess > secret_number:
                print("Try a lower number.")
            else:
                print(f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()
