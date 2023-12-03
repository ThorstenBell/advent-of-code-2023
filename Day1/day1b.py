import re

txt_file_path = 'day1data.txt'
digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
num_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

lines_array = []
with open(txt_file_path, 'r') as file:
    for line in file:
        lines_array.append(line.strip())

results_array = []
for line in lines_array:
    linenum = ""
    indices = []
    for index, char in enumerate(line):
        if char.isdigit():
            indices.append({"num": char, "index": index})
    for digit in digits:
        digit_indices = [match.start() for match in re.finditer(digit, line)]
        for index in digit_indices:
            indices.append({"num": num_dict[digit], "index": index})
    max_num = max(indices, key=lambda x: x['index'])['num']
    min_num = min(indices, key=lambda x: x['index'])['num']
    results_array.append(str(min_num) + str(max_num))

total = 0
for result in results_array:
    total += int(result)

print(total)
