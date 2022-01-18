# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# no considerations for exceptions in leap years

# if year % 4 == 0:
#     print("This is a leap year")
# else:
#     print("this is not a leap year")


# should be able to refactor this for smaller code base but how...I'm dumb 😒 


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("not a leap year")
else:
    print("not a leap year")

# if year % 100 == 0 and year % 400 == 0 or year % 4 == 0:
#     print("leap year")
# else:
#     print("not leap year")






















###### failed attempts from not reading fully vvvv #######


##### LEARN TO READ INSTRUCTIONS FULLY ####### 

# if year % 4 == 0:
#     if year % 100 == 0 or year % 1000 == 0:
#         print("This is not a leap year.")
#     else:
#         print("This is a leap year.")
# else:
#     print("This is not a leap year.")

# if year % 4 == 0 or year % 400 == 0:
#     print("this is a leap year")
# elif year % 100 == 0:
#     print("not a leap year")
# else:
#     print("not a leap year")

# if year % 4 == 0:
#     if year % 100 == 0 and year % 400 == 0:
#         print("leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("not a leap year")