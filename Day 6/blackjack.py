# import stuff
import random


# vars/lists (player/cpu hand, player,cpu value)
deck = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]

player_hand = []

player_total = 0

temp = ""

cpu_hand = []

cpu_total = 0

# Welcome message
print("Blackjack Trainer v0.1")

# issue players first card and remove card from deck

# player first card
player_hand.append(deck[random.randint(0, len(deck) - 1)])
deck.remove(player_hand[0])
player_total += int(player_hand[0])

# shuffle deck
random.shuffle(deck)

# player second card
player_hand.append(deck[random.randint(0, len(deck) - 1)])
player_total += int(player_hand[1])
deck.remove(player_hand[1])

# shuffle deck
random.shuffle(deck)

# cpu first card
cpu_hand.append(deck[random.randint(0, len(deck) - 1)])
cpu_total += int(cpu_hand[0])
deck.remove(cpu_hand[0])

# shuffle deck
random.shuffle(deck)

# cpu second card
cpu_hand.append(deck[random.randint(0, len(deck) - 1)])
cpu_total += int(cpu_hand[1])
deck.remove(cpu_hand[1])

print(player_hand)
print(player_total)
print(cpu_hand)
print(cpu_total)


# issue players second card and remove card from deck

# display cards to user

# issue cpu face up card

# display face up card and face down card

# if user has blackjack, win game

# ask if they want to stand or hit

# loop draw new card and remove from deck if user hits until stand/bust

# if user stand dealer show face down card

# if blacjack, dealer wins

# if dealer < 16 hit and remove from deck, if >= 17 stand,



# display winner


# print(f"Your hand was {player_hand} (Total: {player_total})")
# print(f"CPU hand was {cpu_hand} (Total: {cpu_total}")