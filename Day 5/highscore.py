# 🚨 Don't change the code below 👇
from re import TEMPLATE
from string import Template


student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# print highest score in list
print(f" {max(student_scores)} max()")

# print lowest score in list
print(f" {min(student_scores)} min()")

# maximum score without max()

# temp = 0
max_score = 0
min_score = 0

# highest score without max()
for scores in student_scores:
    # temp = x
    if scores > max_score:
        max_score = scores


# terrible lowest score without min()
for scores in student_scores:
    if scores < student_scores[+1]:
        min_score = scores

# display highest score and lowest score
print(f"The highest score in the class is: {max_score}")
print(f"The lowest score in the class is: {min_score}")