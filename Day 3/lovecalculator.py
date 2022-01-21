# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# converting both names to lowercase and declaring and setting true and love variable to 0
lower1 = name1.lower()
lower2 = name2.lower()
true = 0
love = 0


# limiting this to the functions suggested, checking each name for occurance of certain letters
true = lower1.count("t") + lower1.count("r") + lower1.count("u") + lower1.count("e")
love = lower1.count("l") + lower1.count("o") + lower1.count("v") + lower1.count("e")

true += lower2.count("t") + lower2.count("r") + lower2.count("u") + lower2.count("e")
love += lower2.count("l") + lower2.count("o") + lower2.count("v") + lower2.count("e")


# combining result of previous step and converting to an integer
score = int(f"{true}{love}")


# outputting message with result depending on score achieved
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")