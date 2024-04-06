def is_valid_guess(guess, guessed_letters):
    # Check if the guess is a single letter and hasn't been guessed already
    return len(guess) == 1 and guess.isalpha() and guess not in guessed_letters

def process_guess(word, guessed_letters, guess):
    # Add the guess to the list of guessed letters
    guessed_letters.append(guess)
    # Check if the guess is in the word
    if guess in word:
        print("Correct guess!")
    else:
        print("Incorrect guess!")

def main():
    # Example word
    word = "hangman"
    # List to store guessed letters
    guessed_letters = []

    print("Welcome to the Hangman game!")

    while True:
        # Display the word with blanks for each letter that hasn't been guessed
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("Word:", display_word)

        # Get the player's guess
        guess = input("Enter a letter guess: ").lower()

        # Validate the guess
        if not is_valid_guess(guess, guessed_letters):
            print("Invalid guess. Please enter a single letter that hasn't been guessed already.")
            continue

        # Process the guess
        process_guess(word, guessed_letters, guess)

        # Check if the player has guessed all letters in the word
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

if __name__ == "__main__":
    main()
