import random

# variables
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

# nested list for ascii hand art

hands = [rock, paper, scissors]

# names of the hand to add some shazam to the results

hand_text = ["rock", "paper", "scissors"]

# player asked to pick a hand between 1-3 and subtracts 1 from it for ease of use instead of 0-2

player = int(input("Pick a hand, Type 1 for Rock, 2 for Paper or 3 for Scissors")) - 1

# cpu picks random number between 0 and 2 which decides the hand it draws

cpu = random.randint(0, 2)

# working out who won and displaying results

if (player == 0 and cpu == 0) or (player == 1 and cpu == 1) or (player == 2 and cpu == 2):
    print(f"You picked {hand_text[player]} \n {hands[player]}")
    print(f"CPU picked {hand_text[cpu]} \n {hands[cpu]}")
    print(f"You both picked {hand_text[player]}, It's a draw! 😲")

elif (player == 0 and cpu == 2) or (player == 1 and cpu == 0) or (player == 2 and cpu == 1):
    print(f"You picked {hand_text[player]} \n {hands[player]}")
    print(f"CPU picked {hand_text[cpu]} \n {hands[cpu]}")
    print(f"{hand_text[player]} beats {hand_text[cpu]}, You win! 🥳")
else:
    print(f"You picked {hand_text[player]} \n {hands[player]}")
    print(f"CPU picked {hand_text[cpu]} \n {hands[cpu]}")
    print(f"{hand_text[cpu]} beats {hand_text[player]}, You lost 😥")
