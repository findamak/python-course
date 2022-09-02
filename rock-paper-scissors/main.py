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

# Write your code below this line 👇

# 0 - rock, 1 - paper, 2 scissors
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

list_of_choices = [rock, paper, scissors]

# catch invalid inputs
if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number.")
else:
    # print your choice
    print("You chose:\n")
    print(list_of_choices[player_choice])

    # print computer choice
    print("Computer chose:\n")
    print(list_of_choices[computer_choice])

    if computer_choice == 2 and player_choice == 0:
        # you win
        print("You win.")
    elif computer_choice == 0 and player_choice == 2:
        # computer wins
        print("You lose.")
    elif computer_choice > player_choice:
        # computer wins
        print("You lose.")
    elif player_choice > computer_choice:
        # player wins
        print("You win.")
    elif computer_choice == player_choice:
        # draw
        print("Draw.")




