#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# ask price > tip precent > group size > calculate split > print split

print("Welcome to tip calculator ver 0.01")
price = round(float(input("How much is the bill? ")), 2) #round to 2 in case of user typo

tip_percent = float(input("Do you want to tip 10, 12 or 15%? ")) #implement error on wrong entered number

group_size = float(input("How many people is it being split with? ")) #only allow integer


# (total / people) * tip_percent

# total = float((price / group_size) * float(1.0 + tip_percent))


tip_tester = price * tip_percent / group_size / 100

total_price = price / group_size + tip_tester

print(f"Each person should pay: ${round(total_price, 2)}")

# print(f"the bill split is {split}")
# print(f"the tip amount is {amount}")
# print(f"the total per person is {total}")124.56
