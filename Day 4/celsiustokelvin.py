celsius_values = [5.2, 3.1, 0.1]

output_list = []



for x in range(len(celsius_values)):
    output_list.append(round(celsius_values[x] + 273.15, 2))
print(output_list)