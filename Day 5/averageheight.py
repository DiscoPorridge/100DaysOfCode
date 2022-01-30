# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# can't use len() or sum()

students = 0
total_height = 0
average_height = 0

for x in student_heights:
    total_height += x
    students += 1


average_height = "{:.0F}".format(total_height / students)

print(average_height)