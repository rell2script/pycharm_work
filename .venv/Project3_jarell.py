import random


words = ["house", "apple", "planet", "python", "garden", "bridge"]
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6


def display_word():
    #Print the secret word with unguessed letters hidden.
    displayed_letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            displayed_letters.append(letter)
        else:
            displayed_letters.append("_")
    print(" ".join(displayed_letters))


def check_game_status():
    #Return 'won', 'lost', or 'continue' based on the current game state.
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You guessed the word!")
        print("Final word:")
        display_word()
        return "won"

    if incorrect_guesses >= max_guesses:
        print("Game over! You ran out of guesses.")
        print(f"The secret word was: {secret_word}")
        return "lost"

    return "continue"


def play_game():
    #Run one complete Hangman game.
    global incorrect_guesses

    while True:
        print("\nSecret word:")
        display_word()
        print(f"Guessed letters: {guessed_letters}")
        print(f"Incorrect guesses remaining: {max_guesses - incorrect_guesses}")

        guess = input("Enter a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)
        if guess in secret_word:
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess!")

        status = check_game_status()
        if status != "continue":
            break


if __name__ == "__main__":
    play_game()
