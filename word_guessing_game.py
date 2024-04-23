# Word guessing game

import random

players = ["Player 1", "Player 2"]
word_bank = ["pencil", "highlighter", "desk", "backpack", "crayons", "ruler"]
guessed_letters = []
word_guess_attempts = {player: 0 for player in players}
letter_guess_attempts = {player: 0 for player in players}
remaining_words = word_bank

# function for the guessing of letters
def letters_to_guess(letter, word_to_guess):
    global guessed_letters
    if letter in guessed_letters:
        print("You already guessed that letter!")
        return
    guessed_letters.append(letter)
    if letter in word_to_guess:
        occurrences = word_to_guess.count(letter)
        print(f"The letter '{letter}' is in the word {occurrences} time{'s' if occurrences != 1 else ''}.")
    else:
        print(f"The letter '{letter}' is not in the word.")


# true functionality of the game through player turns, letter and word guesses/attempts
def player_turns(player, word_to_guess):
    global guessed_letters
    print(f"The secret word has {len(word_to_guess)} letters.")
   

    while True:
        guess = input("Guess a letter or the whole word: ").lower()
        if len(guess) == 1:
            letter_guess_attempts[player] += 1
            letters_to_guess(guess, word_to_guess)
        else:
            word_guess_attempts[player] += 1
            if guess == word_to_guess:
                print(f"Congratulations! {player} guessed the word '{word_to_guess}' in {letter_guess_attempts[player]} turns!")
                final_score = letter_guess_attempts[player]
                print(f"Final score: {final_score}")
                return
            else:
                print("Incorrect word guess!")
                if word_guess_attempts[player] == 3:
                    print(f"{player} has used all 3 word guesses (all wrong) and lost the turn!")
                    return
           
# actual execution of the word guessing game, calls function of player turns function at the end
def word_game():
    while remaining_words: # while words still remain 
        word_to_guess = random.choice(remaining_words)
        remaining_words.remove(word_to_guess)
       
        for player in players:
            print(f"It's {player}'s turn!")
            player_turns(player, word_to_guess)

# Example usage of program
word_game()
