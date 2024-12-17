import os
import random

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to select a word from the static list
def select_word():
    word_list = ["MERCURY", "VENUS", "EARTH", "MARS", "JUPITER", "SATURN", "URANUS", "NEPTUNE", "PLUTO", "COMET"]
    return random.choice(word_list)

# Function to display the current state of the word
def display_word(word, correct_guesses):
    return ' '.join([letter if letter in correct_guesses else '_' for letter in word])

# Function to display the hangman based on incorrect guesses
def display_hangman(incorrect_guesses):
    hangman_stages = [
        """
           ------
           |    |
           |    
           |   
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |    
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |    
        --------
        """
    ]
    print(hangman_stages[len(incorrect_guesses)])

# Function to display the current game state
def display_game_state(current_display, incorrect_guesses, total_guesses, max_guesses):
    display_hangman(incorrect_guesses)
    print(f"Current word: {current_display}")
    print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
    print(f"Total guesses made: {total_guesses}")
    print(f"Mistakes remaining: {max_guesses - len(incorrect_guesses)}")

# Function to get the player's guess
def get_player_guess(guessed_letters):
    while True:
        guess = input("Enter a letter: ").strip().upper()
        if len(guess) != 1 or not guess.isalpha() or guess in guessed_letters:
            print("Invalid guess. Please enter a single letter that you haven't guessed yet.")
        else:
            guessed_letters.add(guess)
            return guess

# Function to update the game state based on the player's guess
def update_game_state(guess, word, correct_guesses, incorrect_guesses, guessed_letters):
    if guess in word:
        correct_guesses.append(guess)
    else:
        incorrect_guesses.append(guess)

# Function to check the game status (win/lose)
def check_game_status(correct_guesses, incorrect_guesses, word):
    if set(correct_guesses) == set(word):
        print("Congratulations! You've guessed the word!")
        return True
    if len(incorrect_guesses) >= 6:
        print(f"Game over! The word was: {word}")
        return True
    return False

# Function to ask if the player wants to play again
def ask_to_play_again():
    while True:
        replay = input("Do you want to play again? (Y/N): ").strip().upper()
        if replay in ('Y', 'N'):
            return replay == 'Y'  # Returns True if 'Y', False if 'N'
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

# Main function to play the game
def play_game():
    while True:
        word = select_word()
        correct_guesses = []
        incorrect_guesses = []
        guessed_letters = set()
        max_incorrect_guesses = 6
        total_guesses = 0

        while True:
            clear_screen()
            current_display = display_word(word, correct_guesses)
            display_game_state(current_display, incorrect_guesses, total_guesses, max_incorrect_guesses)

            guess = get_player_guess(guessed_letters)
            update_game_state(guess, word, correct_guesses, incorrect_guesses, guessed_letters)

            total_guesses += 1

            if check_game_status(correct_guesses, incorrect_guesses, word):
                break

        # Call the new function to ask about replaying
        if not ask_to_play_again():
            print("Thanks for playing! Goodbye!")
            break

# Entry point to start the game
if __name__ == "__main__":
    play_game()

