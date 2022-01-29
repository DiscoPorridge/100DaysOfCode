import random

# variables
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
hands = [rock, paper, scissors]

player = int(input("Pick a hand, Type 1 for Rock, 2 for Paper or 3 for Scissors")) - 1
#Write your code below this line 👇

