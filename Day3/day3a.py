import re

txt_file_path = 'data.txt'
data = []

with open(txt_file_path, 'r') as file:
    for line in file:
        data.append(line.strip())

numbers = []
string_length = 0
pattern = r'\d+'

for index, string in enumerate(data):
    string_length = len(string) - 1
    matches = [(match.start(), match.group()) for match in re.finditer(pattern, string)]
    for match in matches:
        indices = []
        for i in range(len(match[1])):
            indices.append(match[0] + i)
        number = {
            "number": match[1],
            "row": index,
            "indices": indices
        }
        numbers.append(number)


def is_symbol(char):
    return char.isalnum() or char == "."


def check_for_symbols(elem):
    search_rows = [elem['row']]
    search_indices = list(elem['indices'])
    if elem['row'] > 0:
        search_rows.append(elem['row'] - 1)
    if elem['row'] < (len(data) - 1):
        search_rows.append(elem['row'] + 1)
    if min(elem['indices']) > 0:
        search_indices.append(min(elem['indices']) - 1)
    if max(elem['indices']) < string_length:
        search_indices.append(max(elem['indices']) + 1)
    for search_row in search_rows:
        for search_index in search_indices:
            if not is_symbol(data[search_row][search_index]):
                return True

    return False


result_array = []
for number in numbers:
    if check_for_symbols(number):
        result_array.append(int(number["number"]))

print(sum(result_array))

# wrong results 508068, 507281, 229382
