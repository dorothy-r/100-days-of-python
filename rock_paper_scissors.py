import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

player = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))

if player < 0 or player > 2:
    print("ERROR")
else:
    print(game_images[player])

computer = random.randint(0, 2)

print("Computer chose:")
print(game_images[computer])


if player == computer:
    print("It's a draw.")
elif (computer == 0 and player == 1) or (computer == 1 and player == 2) or (computer == 2 and player == 0):
    print("You win!")
else:
    print("You lose.")
