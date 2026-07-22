'''
Write a program to build Rock, Paper and Scissors game
1. Rock wins against scissors
2. Scissors win against paper
3. Paper wins against rock
'''

import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

user_choice = input("What do you choose? Rock, Paper or Scissors\n")
if user_choice == "Rock":
    print(rock)
elif user_choice == "Paper":
    print(paper)
elif user_choice == "Scissors":
    print(scissors)

random_list = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(random_list)
print(f"computer_choice: {computer_choice}")
if computer_choice == "Rock":
    print(rock)
elif computer_choice == "Paper":
    print(paper)
elif computer_choice == "Scissors":
    print(scissors)

if user_choice == "Rock" and computer_choice == "Scissors":
    print(f"Rock Wins! {rock}")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print(f"Scissors Wins! {scissors}")
elif user_choice == "Paper" and computer_choice == "Rock":
    print(f"Paper Wins! {paper}")
elif user_choice == "Rock" and computer_choice == "Paper":
    print(f"Paper Wins! {paper}")
elif user_choice == "Paper" and computer_choice == "Scissors":
    print(f"Scissors Wins! {scissors}")
elif user_choice == "Scissors" and computer_choice == "Rock":
    print(f"Rock Wins! {rock}")
elif user_choice == computer_choice:
    print("There is a tie. Play Again")



