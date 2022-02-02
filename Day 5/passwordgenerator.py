#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

# overkill for seed generation for this, uses system time at first then random number between 2 reasonably large (for this) prime numbers
random.seed(random.randint(2197172813311000729512343216125642781, 90000000000000000006160000000000000000009))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# loops requested amount of letters and adds random letters to password
for potato in range(nr_letters):
    password += letters[random.randint(0, 51)]

# I think initialising seed() before each loop will increase the randomness of output ...🤔
random.seed(random.randint(2197172813311000729512343216125642781, 90000000000000000006160000000000000000009))

# loops requested amount of symbols and adds random symbols to end of letters
for potato in range(nr_symbols):
    password+= symbols[random.randint(0, 8)]

# same as above
random.seed(random.randint(2197172813311000729512343216125642781, 90000000000000000006160000000000000000009))

# loops requested amount of numbers and adds random numbers to end of symbols
for potato in range(nr_numbers):
    password += numbers[random.randint(0, 9)]

# outputs generated password with users requirements
print(f"generated password: {password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P