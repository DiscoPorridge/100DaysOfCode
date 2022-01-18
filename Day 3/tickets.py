print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? \n"))
age = int(input("How old are you? \n"))

# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("you are not tall enough to ride the rollercoaster")

if height >= 120:
    if age >= 18:
        print("You are tall enough to ride the rollercoaster, Tickets cost $12")
    elif age >= 12 and age < 18:
        print("You are tall enough to ride the rollercoaster, Tickets cost $7")
    else:
        print("You are tall enough to ride the rollercoaster, Tickets cost $5")
else:
    print("You are not tall enough to ride the rollercoaster! :(")