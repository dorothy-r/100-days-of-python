import random
from art import logo
############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


def deal_card():
    """Return a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Take a list of cards and return the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(score1, score2):
    """Compares two players' scores and determines the outcome"""
    if score1 == score2:
        return "Draw 🙃"
    elif score1 == 0:
        return "You win with a blackjack 😎"
    elif score2 == 0:
        return "You lose, opponent has Blackjack 😱"
    elif score1 > 21:
        return "You went over. You lose 😭"
    elif score2 > 21:
        return "Opponent went over. You win 😁"
    elif score1 > score2:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(f'\33c')
    print(logo)

    game_over = False
    user_cards = []
    computer_cards = []

    # Deal the user and computer 2 cards each
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Calculates scores and allows users to add more cards until conditions for game_over are met
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            hit_me = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit_me == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    # Computer draws more cards if score is < 17
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    print(compare(user_score, computer_score))


while input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
