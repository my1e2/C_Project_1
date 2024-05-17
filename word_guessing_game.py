# word guessing game

import random
import pandas as pd
import matplotlib.pyplot as plt

players = ["Player 1", "Player 2"]  # list for players
word_bank = ["pencil", "highlighter", "desk", "backpack", "crayons", "ruler"]  # list for school supplies word bank
scores = {player: [] for player in players}  # dictionary to keep track of scores for each player

# Function for guessing letters
def letters_to_guess(letter, word_to_guess, guessed_letters):
    if letter in guessed_letters:
        print("You already guessed that letter!")
        return False
    guessed_letters.append(letter)
    if letter in word_to_guess:
        occurrences = word_to_guess.count(letter)
        print(f"The letter '{letter}' is in the word {occurrences} time{'s' if occurrences != 1 else ''}.")
    else:
        print(f"The letter '{letter}' is not in the word.")
    return True

# Function to handle player turns, letter and word guesses/attempts
def player_turns(player, word_to_guess):
    guessed_letters = []  # Reset guessed letters for each player after they win or lose word guessing of one word
    letter_guess_attempts = 0  # Reset letter guess attempts after they win or lose word guessing of one word
    word_guess_attempts = 0  # Reset word guess attempts after they win or lose word guessing of one word

    print("The theme is school supplies!!!")
    print(f"The secret word has {len(word_to_guess)} letters.")

    while True:
        guess_letter = input("Guess a letter: ").lower()
        if len(guess_letter) == 1:
            letter_guess_attempts += 1
            if not letters_to_guess(guess_letter, word_to_guess, guessed_letters):
                continue

            guess_word_prompt = input("Do you want to guess the word? (yes/no): ").lower()
            if guess_word_prompt == "yes":
                word_guess_attempts += 1
                guess_word = input("Guess the word: ").lower()
                if guess_word == word_to_guess:
                    print(f"Congratulations! {player} guessed the word '{word_to_guess}' "
                          f"in {letter_guess_attempts} letter guesses and {word_guess_attempts} word guesses!")
                    final_score = letter_guess_attempts
                    scores[player].append(final_score)
                    print(f"Final score: {final_score}")
                    break
                elif word_guess_attempts == 3:
                    print(f"{player} has used all 3 word guesses (all wrong) and lost!")
                    scores[player].append(float('inf'))  # Record an infinite score for failing to guess (lets us plot data points)
                    break # move on to the next player's turn and reset guesses
                else:
                    print("Wrong word guess")
        else:
            print("Invalid input. Please guess a single letter.")

# Function to analyze and plot scores
def analyze_and_plot_scores():
    scores_dataframe = pd.DataFrame(data = scores) # connecting data frame and dictionary for players and their scores
    scores_dataframe.plot(kind='bar')
    plt.xlabel('Round Number')
    plt.ylabel('Score (Lower is Better)')
    plt.title('Player Scores')
    plt.legend(title='Players')
    plt.show()

# Actual execution of the word guessing game
def word_game():
    remaining_words = word_bank.copy()  # assigning a copy of the word bank list to remaining words variable so that I don't alter original list of words

    while remaining_words:  # while words still remain
        word_to_guess = random.choice(remaining_words)
        remaining_words.remove(word_to_guess)

        for player in players:
            print(f"It's {player}'s turn!")
            player_turns(player, word_to_guess)

    if not remaining_words:
        print("No more words left to guess, game over!")

    # Analyze and plot scores
    analyze_and_plot_scores()

# Example usage of the program
word_game()
