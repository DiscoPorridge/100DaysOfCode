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
print(f"First card: {player_hand[0]}")

# shuffle deck
random.shuffle(deck)

# player second card
player_hand.append(deck[random.randint(0, len(deck) - 1)])
player_total += int(player_hand[1])
deck.remove(player_hand[1])
print(f"Second card: {player_hand[1]}")


# shuffle deck
random.shuffle(deck)

# cpu first card
cpu_hand.append(deck[random.randint(0, len(deck) - 1)])
cpu_total += int(cpu_hand[0])
deck.remove(cpu_hand[0])
print(f"Dealer face up card: {cpu_hand[0]}")

# shuffle deck
random.shuffle(deck)

# cpu second card
cpu_hand.append(deck[random.randint(0, len(deck) - 1)])
cpu_total += int(cpu_hand[1])
deck.remove(cpu_hand[1])
print(f"Dealer face down card")

print(f"Your hand is {player_hand[0]} and {player_hand[1]} (Total: {player_total})")

if player_total == 21:
    print(f"You got BlackJack ({player_hand[0]} {player_hand[1]})")
    print(f"Dealer hand: {cpu_hand[0]} {cpu_hand[1]}")

hit = input("Do you want to [H]it or [S]tand?")

if hit == "S" or hit == "s":
    print("You have decided to Stand")
    print(f"Dealers hand is {cpu_hand[0]} {cpu_hand[1]}")


    if cpu_total > 17:
        print("Dealer stands")
        if cpu_total > player_total:
            print(f"You have {player_hand[0]} and {player_hand[1]} (Total: {player_total} and Dealer has {cpu_hand[0]} and {cpu_hand[1]} (Total: {cpu_total}")
            print("You lost")
        else:
            print("You Won!")
            print(f"You have {player_hand[0]} and {player_hand[1]} (Total: {player_total} and Dealer has {cpu_hand[0]} and {cpu_hand[1]} (Total: {cpu_total}")

    else:
        while cpu_total < 17:
            cpu_hand.append(deck[random.randint(0, len(deck) - 1)])



        if cpu_total > 21:
            print("You won, Dealer went Bust")

# ask if they want to stand or hit

# loop draw new card and remove from deck if user hits until stand/bust

# if user stand dealer show face down card

# if blacjack, dealer wins

# if dealer < 16 hit and remove from deck, if >= 17 stand,



# display winner


# print(f"Your hand was {player_hand} (Total: {player_total})")
# print(f"CPU hand was {cpu_hand} (Total: {cpu_total}")