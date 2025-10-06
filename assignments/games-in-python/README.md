

# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman game in Python to practice string manipulation, loops, conditionals, and random selection. You will create an interactive word-guessing game where players try to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️	Hangman Game Logic

#### Description
Create the core logic for a Hangman game. The program should randomly select a word from a predefined list, accept letter guesses from the user, and display the current progress of the word using underscores for unguessed letters.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept single-letter guesses from the user
- Display the current progress (e.g., _ a _ _ m a n)
- Track and display the number of incorrect guesses remaining
- End the game when the word is guessed or attempts are exhausted
- Display a win or lose message at the end

Example:
```plaintext
Word: _ _ _ _ _ _ _
Guess a letter: a
Word: _ a _ _ _ a _
Incorrect guesses left: 5
...etc...
```

### 🛠️	Replay and Word List Enhancement

#### Description
Enhance your Hangman game by allowing the player to play multiple rounds and by expanding the word list. Add an option for the player to play again after each game, and use a list of at least 10 words.

#### Requirements
Completed program should:

- Ask the player if they want to play again after each game
- Use a word list with at least 10 different words
- Reset the game state for each new round
