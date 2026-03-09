# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python that practices string manipulation, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️ Build the game engine

#### Description
Create the core Hangman gameplay loop that selects a random word, accepts letter guesses from the player, and updates the displayed progress.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Display the current word progress using underscores for unknown letters (e.g., `_ _ a _ _`).
- Accept single-letter guesses and update the progress when correct.
- Track and display remaining incorrect guesses.
- Prevent the same letter from being guessed twice.

### 🛠️ Handle win/lose conditions

#### Description
Determine when the player has won or lost, then display a clear end-of-game message.

#### Requirements
Completed program should:

- End the game when the player guesses all letters correctly (win).
- End the game when the player runs out of attempts (lose).
- Display a win message with the completed word.
- Display a lose message and reveal the word.
- Offer a clear prompt for the player to play again (optional enhancement).
