# 🚨 Don't change the code below 👇
from re import TEMPLATE
from string import Template


student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# temp = 0
max_score = 0

for scores in student_scores:
    # temp = x
    if scores > max_score:
        max_score = scores
print(f"The highest score in the class is: {max_score}")