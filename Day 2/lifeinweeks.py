# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# life = 90, 365 days, 52 weeks, 12 months

# remaining = 90 - int(age)
months = (90 - int(age)) * 12
weeks = (90 - int(age)) * 52
days = (90 - int(age)) * 365

#You have 12410 days, 1768 weeks, and 408 months left.

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
