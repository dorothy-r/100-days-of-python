import random
from art import logo, vs
from game_data import data


def compare(account_a, account_b):
    """Compares follower count of two accounts and returns the winner"""
    if account_a["follower_count"] > account_b["follower_count"]:
        winner = "A"
    else:
        winner = "B"
    return winner


def game():
    game_over = False
    score = 0
    # Generate random accounts
    accounts = random.sample(data, 2)
    account_a = accounts[0]
    account_b = accounts[1]
    # Loop repeats game until user gets an answer wrong
    while not game_over:
        print(logo)
        print(
            f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
        print(vs)
        print(
            f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")

        # Determine which account has higher follower count
        winner = compare(account_a, account_b)

        # Ask user for guess
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        print(f'\33c')

        # Check whether user's guess is correct
        if guess != winner:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True
        else:
            score += 1
            print(f"You're right! Current score: {score}")
            account_a = account_b
            while account_a == account_b:
                account_b = random.choice(data)


game()
