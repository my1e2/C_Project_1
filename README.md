How the program generally works:

My program code allows two players to take turns cycling through the words/letters of a school supplies (hint for possible words) word bank.

Each player has the option to guess what exact letters are in the word at first. The program will also tell you the occurrences of the letter that is inside the word they are checking for. However, it will not expose the position of that letter in the word. It will prompt the user to guess a letter over and over again until they give one. If the user gives the same letter as before in another guess, it will tell them that they already guessed that letter.

Players will then have the option of guessing the word whenever they want to after guessing a letter during their turn to go. 

Program will make sure players guess letters properly.

If you guess a letter you already guessed, the program will give you a chance to guess another letter until you guess a letter you haven't already guessed.

They get 3 wrong word guesses until they have to get it right or they lose the ability to guess the word for that turn. Then it becomes the next player's turn, and each player will continue to guess words/letters until there are no more words left to guess.

Displays the amount of letter guesss and word guesses it took for the players to guess the final word correctly.

Displays final cumulative score after each player is done guessing the words (a lower score is better, which means the player took fewer letter guesses to get the correct answer).

The amount of letter guesses and word guesses is reset for the next player after the other player either guesses the word correctly, or guesses the word wrong 3 times. 

Each time after word is guessed, a new "round" begins until the game is eventually over after all words are guessed for both players.

At the end of all the "rounds" for both players, a bar plot graph is displayed to show the score of both players over each round.

How to run the program (code):
1. Begin executing the program and guess a letter after being told that it's "Player 1's turn", with the "theme as school supplies".
2. Guess a possible letter within the randomly selected word from the school supplies word bank.
3. If you guess a word instead of a letter (spaces within input for letter), the program will tell you "Invalid input. Please guess a single letter." until you guess properly.
4. The program will then tell you if the letter was found in the word from the school supplies word bank, and if it was found, it will tell you exactly how many times it was found.
5. If the letter was not found, the program will tell you that the letter is not in the word.
6. If you guess a letter you already guessed, the program will tell you that "you already guessed that letter!" and prompt you to guess a letter again.
7. It will then ask if you want to guess the word now, and give you the option of saying 'yes' or 'no' (any answer other than yes will automatically default to no).
8. If you guess incorrectly, the program will tell you "Wrong word guess", and ask you to guess a letter again.
9. If you guess correctly, the program will tell you "Congratulations, Player 1/2 guessed the word" in however many "letter guesses" or "word guesses" it took for them to get it right.
10. It will then give the player a final score that corresponds to the number of letter guesses it took before getting the word guess correct.
11. Afterwards, it will move on to the next player's turn, and the process will start all over again from steps 1-2.
12. In the case that the player guesses the wrong word 3 times in a row, the player will lose the opportunity to guess that word further and it will be the next player's turn.
13. If the players both make it through all the words in the word bank, the program will quit and tell them "There are no more words left to guess, game over!"
14. At the end, a bar plot graph will dispaly the scores of each player over the 6 rounds of word guessing (lower scores/bars are better, means it took less letter guesses for correct guess).
