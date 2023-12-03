import re

txt_file_path = 'day3data.txt'
data = []

with open(txt_file_path, 'r') as file:
    for line in file:
        data.append(line.strip())

numbers = []
string_length = 0
pattern = r'\d+'

for index, string in enumerate(data):
    string_length = len(string) - 1
    matches = re.findall(pattern, string)
    existing = []
    for match in matches:
        match_indices = [x.start() for x in re.finditer(match, string)]
        first_index = string.find(match)
        if len(match_indices) > 1:
            if match in existing:
                new_index = existing.count(match)
                first_index = match_indices[new_index]
            existing.append(match)
        indices = []
        for i in range(len(match)):
            indices.append(first_index + i)
        number = {
            "number": match,
            "row": index,
            "indices": indices
        }
        numbers.append(number)


def is_symbol(char):
    return char.isalnum() or char == "."


def check_for_symbols(elem):
    search_rows = [elem['row']]
    search_indices = elem['indices']
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

# wrong results 508068, 507281