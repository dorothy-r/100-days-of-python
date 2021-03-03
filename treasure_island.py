print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First decision point
print("You follow a path into the jungle. Soon, it splits into two. Which fork will you choose?")
choice_1 = input("Type 'left' or 'right'\n").lower()

# Second decision point
if choice_1 == "left":
    print("You arrive at a large lake with an island in the middle. You can see a boat making its way to the shore where you stand. Do you wait for the boat or swim to the island?")
    choice_2 = input("Type 'swim' or 'wait'\n").lower()

    # Third decision point
    if choice_2 == "wait":
        print("The woman sailing the boat offers to take you across to the island, warning you about the mermaids in the water. When you arrive, you wander around the island until you find an old stone building with three doors. Each door has been painted a different color. Which door will you enter?")
        choice_3 = input("Type 'red', 'yellow', or 'blue'\n").lower()

        if choice_3 == "red":
            print("Oh no! The building catches on fire! Game over.")
        elif choice_3 == "blue":
            print(
                "Oh no! A pack of wild animals emerge and chase you back to the boat! Game over.")
        elif choice_3 == "yellow":
            print("You found the treasure! Congratulations, you win!")
    else:
        print("You encounter a group of mermaids who ask you to stay with them. When you learn that they can make you a mermaid, too, you agree and abandon your search for the treasure. Game Over.")
else:
    print("You wander through the jungle for days before you are rescued, and never find the treasure. Game over.")
