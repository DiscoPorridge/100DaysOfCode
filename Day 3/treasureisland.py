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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

start = input("You\'re at a crossroad, go left or right? \n").lower()

print(f"You have selected {start}")

if start == "left":
    river = input("you reach a river, swim across or wait for the boat? \n").lower()
    print(f"you have decided to {river}")
    if river == "wait":
        print("You cross the river in the boat")
        door = input("you come across 3 doors...which one do you pick? red, blue or yellow \n").lower()
        print(f"you have picked the {door} door")
        if door == "red":
            print("You open the door and a stampede of beasts devour you.")
            print("Game over")
        elif door == "blue":
            print("You open the door and raging flames burn you to death.")
            print("Game Over")
        elif door == "yellow":
            print("You found the treasure!")
        else:
            print("A rock slips from the ceiling and kills you.")
            print("Game Over")
    else:
        print("A mutant trout appears from the murky water and eats you.")
        print("Game Over")
else:
    print("You stumble around and fall into an spike ridden hole.")
    print("You die.")
    print("Game Over")
