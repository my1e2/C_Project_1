# word guessing game

import random

players = ["Player 1", "Player 2"] # list for players
word_bank = ["pencil", "highlighter", "desk", "backpack", "crayons", "ruler"] # list for school supplies word bank
guessed_letters = [] # list for letters guessed so far
word_guess_attempts = {player: 0 for player in players} # dictionary to keep track of player word guesses, key is player
letter_guess_attempts = {player: 0 for player in players} # dictionary to keep track of player letter guesses, key is player
remaining_words = word_bank # assigning word bank list to remaining words variable to alter it after a word is guessed (cycle through)

# Function for guessing letters
def letters_to_guess(letter, word_to_guess):
    global guessed_letters # list accessible in this function now 
    if letter in guessed_letters:
        print("You already guessed that letter!")
        return
    guessed_letters.append(letter)
    if letter in word_to_guess:
        occurrences = word_to_guess.count(letter)
        print(f"The letter '{letter}' is in the word {occurrences} time{'s' if occurrences != 1 else ''}.")
    else:
        print(f"The letter '{letter}' is not in the word.")
    
    

# Function to handle player turns, letter and word guesses/attempts
def player_turns(player, word_to_guess):
    global guessed_letters # list accessible in this function now
    print("The theme is school supplies!!!")
    print(f"The secret word has {len(word_to_guess)} letters.")
    letter_guess_attempts[player] = 0  # Reset letter guess attempts after they win or lose word guessing of one word
    word_guess_attempts[player] = 0  # Reset word guess attempts after they win or lose word guessing of one word
    guessed_letters = [] # Reset guessed letters for each player after they win or lose word guessing of one word

    while True:
        guess_letter = input("Guess a letter: ").lower()
        if len(guess_letter) == 1:
            letter_guess_attempts[player] += 1
            letters_to_guess(guess_letter, word_to_guess)

            guess_word = input("Do you want to guess the word? (yes/no): ").lower()
            if guess_word == "yes":
                word_guess_attempts[player] += 1
                guess_word = input("Guess the word: ").lower()
                if guess_word == word_to_guess:
                    print(f"Congratulations! {player} guessed the word '{word_to_guess}' "
                          f"in {letter_guess_attempts[player]} letter guesses and {word_guess_attempts[player]} word guesses!")
                    final_score = letter_guess_attempts[player] 
                    print(f"Final score: {final_score}")
                    return # Will exit the current player's turn and reset guesses
                elif word_guess_attempts[player] == 3:
                        print(f"{player} has used all 3 word guesses (all wrong) and lost!")
                        return # Another scenario that will exit the current player's turn and reset guesses
                elif guess_word != word_to_guess:
                    print(f"Wrong word guess")
                else:
                    break # Will move on to the next player's turn and reset guesses
                

# Actual execution of the word guessing game
def word_game():
    while remaining_words:  # while words still remain
        word_to_guess = random.choice(remaining_words)
        remaining_words.remove(word_to_guess)

        for player in players:
            print(f"It's {player}'s turn!")
            player_turns(player, word_to_guess)
    if not remaining_words:
        print("No more words left to guess, game over!")

# Example usage of the program
word_game()
