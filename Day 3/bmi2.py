# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# It should tell them the interpretation of their BMI based on the BMI value.

#     Under 18.5 they are underweight
#     Over 18.5 but below 25 they have a normal weight
#     Over 25 but below 30 they are slightly overweight
#     Over 30 but below 35 they are obese
#     Above 35 they are clinically obese.

#   Calculation

# answer = round(int(float(weight) / float(height) ** 2)) ### fails with wrong answer


answer = round(weight / height ** 2)

#   Output

if answer > 35:
    print(f"Your BMI is {answer}, you are clinically obese.")

elif answer >= 30 and answer < 35:
    print(f"Your BMI is {answer}, you are obese.")

elif answer >= 25 and answer < 30:
    print(f"Your BMI is {answer}, you are slightly overweight.")

elif answer >= 18.5 and answer < 25:
    print(f"Your BMI is {answer}, you have a normal weight.")

else:
    print(f"Your BMI is {answer}, you are underweight.")

if answer >= 25 and answer < 30:
    print("potato")