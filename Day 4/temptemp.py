# define and initialise temperature and output lists
temperatures = [38.2, 38.3, 39.2]
output = []

# iterate through temperature list until end is reached
for x in range(len(temperatures)):
    # if temperature is less than 38.2 add "L" to output list
    if temperatures[x] < 38.3:
        output.append("L")
    # if temperature is equal or greater than 39.2, add "H" to output list
    elif temperatures[x] >= 39.2:
        output.append("H")
    # else add "N" to output list if temperature is out of range of previous steps
    else:
        output.append("N")

# print the output
print(output)