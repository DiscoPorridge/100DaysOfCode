############## Day 5 Scratchpad ##############


# imported modules

import random


# for loop list
fruits = ["Apple", "Peach", "Pear"]

# for loop - for x in y (operator z):

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)


# # range()

# sum = 0

# for number in range(1, 101):
#     print(f"{sum} + {number} =")
#     sum += number
#     print(f"{sum}")
# print(f"total is {sum}")


# # range() with steps
# sum = 0

# for number in range(1, 101, 10):
#     print(f"{sum} + {number} =")
#     sum += number
#     print(f"{sum}")
# print(f"total is {sum}")


# fizzbuzz stuff 🤢

# fizz = 0
# buzz = 0

# if buzz == 0:
#     print("fizz")
#     buzz = 1
# if fizz == 0:
#     print("buzz")
#     fizz = 1

# if fizz == 1 and buzz == 1:
#     print("fizzbuzz")


# password generator

random.seed(random.randint(2197172813311000729512343216125642781, 90000000000000000006160000000000000000009))

# print(random.random())

# print(random.random())


s = "0123456789"
s[2]
s[4:6]
s[:6]
s[4:]
print(s[random.randint(0, len(s))])