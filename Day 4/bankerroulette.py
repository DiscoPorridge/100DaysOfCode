import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# pick random person from name list

# payee = random.choice(names)

# print(f"{payee} is going to buy the meal today!")

print(f"{random.choice(names)} is going to buy the meal today!")