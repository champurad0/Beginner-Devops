#rock, paper, scissors
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

moves = [rock, paper, scissors]
# rock = 0, paper = 1, scissors = 2
user_move = int(input("Select 1 of the following moves, rock = 0, paper = 1, scissors = 2. \n"))

computer_move = random.randint(0, 2)

if user_move < 0 or user_move >= 3:
 print("You've selected an invalid option.")

if user_move == 0 and computer_move == 2:
    print("you win.")
elif user_move == 1 and computer_move == 0:
    print("you win.")
elif user_move == 2 and computer_move == 1:
    print("you win.")
elif user_move == 2 and computer_move == 0:
    print("you lose.")
elif user_move == 0 and computer_move == 1:
    print("you lose.")
elif user_move == 1 and computer_move == 2:
    print("you lose.")
elif user_move == computer_move:
    print("its a tie")