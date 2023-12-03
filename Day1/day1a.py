txt_file_path = 'day1data.txt'
lines_array = []
with open(txt_file_path, 'r') as file:
    for line in file:
        lines_array.append(line.strip())

results_array = []
for line in lines_array:
    linenum = ""
    for char in line:
        if char.isdigit():
            linenum += char
            break
    for char in reversed(line):
        if char.isdigit():
            linenum += char
            break
    results_array.append(linenum)

total = 0
for result in results_array:
    total += int(result)

print(total)
