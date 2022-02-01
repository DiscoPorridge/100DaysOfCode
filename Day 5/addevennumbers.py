#Write your code below this row 👇

sum = 0


# using range() steps to add every even number to sum
for number in range(1, 101, 2):
    # print(f"{sum} + {number} =")
    sum += number
    # print(f"{sum}")
# print(f"total is {sum}")
print(sum)


# using range() and then if statement modulo returns 0 add number to sum to get same result as above
for number in range(1, 101):
    if number % 2 == 0:
        sum += number
print(sum)