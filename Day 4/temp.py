# initialise temperature and output_list lists
temperatures = [38.2, 38.4, 38.5, 38.6, 39.3]
output_list = []
output_list2 = 0

# iterate through temperature list until the end is reached
for x in range(len(temperatures)):
    # if the temperatures are not outside the low and high breakpoint add +1 to output_list and output_list2
    if not temperatures[x] < 38.3 or temperatures[x] > 39.2:
        output_list.append(+ 1)
        output_list2 += int(1)
# calculate the percentage of temperatures within the the "N" range 
output_list2 = int(output_list2 / len(temperatures) * 100)

# output the result
print(f"{output_list2} % of values are within the normal range")