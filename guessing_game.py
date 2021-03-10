import random

logo = """

   ___                  _   _          _  _            _              
  / __|_  _ ___ ______ | |_| |_  ___  | \| |_  _ _ __ | |__  ___ _ _  
 | (_ | || / -_|_-<_-< |  _| ' \/ -_) | .` | || | '  \| '_ \/ -_) '_| 
  \___|\_,_\___/__/__/  \__|_||_\___| |_|\_|\_,_|_|_|_|_.__/\___|_|   
                                                                      
"""

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS


def guess_compare(guess, answer, attempts):
    """Checks guess against answer, returns number of attempts remaining"""
    if guess == answer:
        print(f"You got it! The answer was {guess}")
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print("Too high")
        return attempts - 1


def game():
    print(logo)
    answer = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    attempts = set_difficulty()

    guess = 0

    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = guess_compare(guess, answer, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose")
            return
        elif guess != answer:
            print("Guess again.")


game()
