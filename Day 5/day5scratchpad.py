############## Day 5 Scratchpad ##############
fruits = ["Apple", "Peach", "Pear"]

# for loop - for x in y (operator z):

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)


# range()

sum = 0

for number in range(1, 101):
    print(f"{sum} + {number} =")
    sum += number
    print(f"{sum}")
print(f"total is {sum}")


# range() with steps
sum = 0

for number in range(1, 101, 10):
    print(f"{sum} + {number} =")
    sum += number
    print(f"{sum}")
print(f"total is {sum}")