# word guessing game

word_bank = ["pencil", "highlighter", "desk", "backpack", "crayons", "ruler"]

print("Try to guess the word! All possible answers deal with school supplies!!")

def letters_to_guess():
    occurences = 0
    while True:
        guessed_letter = input("Guess a possible letter in the words for the word bank: ")
        for guessed_letter in word_bank: # for index in range(len(word_bank)), print(f")
            print(f"This letter appears {occurences} in the words for this word bank.")
            occurences += 1

def word_to_guess():
    attempts = 0
    while True:
       guessed_word = input("Guess: ").casefold
       if guessed_word != word_bank:
           raise ValueError("Wrong word!")
       if guessed_word == word_bank:
           print("Correct guess!")
       elif attempts >= 2:
           print("Thats 3 wrong guesses... You lose!")
       attempts += 1

def player_turns(guessed_word):
    player_one = ""
    player_two = ""
    if guessed_word 

def word_tracking_letter_tracking(guessed_letter, guessed_word):
      while True:
          
def final_score():

if guess != word_bank # if word is not in word bank

# else if word has already been guessed 

# else if guesses = 3, game ends