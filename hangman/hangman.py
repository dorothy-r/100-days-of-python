import random
import hangman_words
import hangman_art


end_of_game = False
lives = 6

print(hangman_art.logo)

# Randomly choose a word from the word_list
chosen_word = random.choice(hangman_words.word_list)

# For each letter in the chosen_word, add a "_" to 'display'.
display = []
for letter in chosen_word:
    display.append("_")

# A while loop to let the user guess again, until the game is over
guesses = []
while not end_of_game:
    # Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()
    print(f'\33c')
    # Let the user know if they've already guessed a letter
    while guess in guesses:
        print(" ".join(display))
        print(f"You've already guessed {guess}")
        print(hangman_art.stages[lives])
        guess = input("Guess a letter: ").lower()
        print(f'\33c')
    guesses.append(guess)

    # Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal it in the display
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    # If guess is not a letter in the chosen_word, reduce lives by one and let user know
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.")

    # Print the display
    print(" ".join(display))

    # Condition to end the game when lives go down to 0
    if lives == 0:
        end_of_game = True
        print(f"Sorry. You lost. The word was {chosen_word}")

    # Condition to end the game when the entire word has been guessed
    if "_" not in display:
        end_of_game = True
        print("You won! Congratulations!")

    # Print the ASCII that corresponds to the current number of 'lives' the user has remaining.
    print(hangman_art.stages[lives])
