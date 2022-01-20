# declaring cost variable and setting to 0
cost = 0

# asking height
height = int(input("how tall are you in cm? \n"))

# checking if person is tall enough to ride the coaster
if height >= 120:
    print("You can ride the rollercoaster")
    # declaring age variable with user input and checking which ticket bricket they are
    # adding ticket price to cost variable
    age = int(input("how old are you?"))
    if age < 12:
        print("Child tickets are $5")
        cost += 5
    elif age < 18:
        print("Teenage tickets are $7")
        cost += 7
    else:
        print("Adult tickets are $12")
        cost += 12
    # declaring photo variable and adding photo price to cost.
    photo = input("Do you want a photo taken for $3? Y or N.")
    if photo == "Y":
        cost += 3
    # outputting total cost of persons ride
    print(f"Your total is {cost} for ticket and photo.")
# letting person know they are too small to ride the coaster
else:
    print("Sorry you are too small to ride the rollercoaster! :(")

# print(f"Your total is {cost} for ticket and photo")

