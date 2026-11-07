#1
import random

def generate_secret_number():
    return random.randint(1, 20)

#2
def play_guessing_game():
    secret_number = generate_secret_number()
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        try:
            guess = int(input("Guess a number between 1 and 20: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        attempts += 1
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number!")
            return

    print(f"You ran out of attempts. The secret number was {secret_number}.")

#3

def play_quick_quiz():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)

    try:
        answer = int(input(f"What is {first_number} + {second_number}? "))
    except ValueError:
        print(f"Please enter a whole number. The correct answer is {first_number + second_number}.")
        return

    if answer == first_number + second_number:
        print("Correct! You earned 1 point.")
    else:
        print(f"Incorrect. The correct answer is {first_number + second_number}.")

#4
def main():
    while True:
        print("===== PYTHON CHALLENGE GAME =====")
        print("1. Play the guessing game")
        print("2. Take a quick math quiz")
        print("3. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            play_guessing_game()
        elif choice == "2":
            play_quick_quiz()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()