import pandas as pd

import sys
sys.setrecursionlimit(20000)


data = pd.read_csv("data.txt", header=None)
unpacked_data = []
for line in data[0]:
    unpacked_data.append([*line])

df = pd.DataFrame(data=unpacked_data)
s_row, s_col = (df == 'S').stack().idxmax()

pipe_rules = {"|": ["north", "south"], "-": ["west", "east"], "L": ["north", "east"], "J": ["north", "west"],
              "7": ["south", "west"], "F": ["south", "east"], ".": [], "S": ["north", "east", "south", "west"]}

pipes_in_loop = {}


def check_north(row, col, step):
    char = df[col][row - 1]
    if char == 'S':
        return
    if 'south' in pipe_rules[char]:
        if (row - 1, col, char) not in pipes_in_loop:
            pipes_in_loop[(row - 1, col, char)] = step + 1
        else:
            pipes_in_loop[(row - 1, col, char)] = min(pipes_in_loop[(row - 1, col, char)], (step + 1))
        if char == "|":
            check_north(row - 1, col, step + 1)
        if char == "7":
            check_west(row - 1, col, step + 1)
        if char == "F":
            check_east(row - 1, col, step + 1)


def check_east(row, col, step):
    char = df[col + 1][row]
    if char == 'S':
        return
    if 'west' in pipe_rules[char]:
        if (row, col + 1, char) not in pipes_in_loop:
            pipes_in_loop[(row, col + 1, char)] = step + 1
        else:
            pipes_in_loop[(row, col + 1, char)] = min(pipes_in_loop[(row, col + 1, char)], (step + 1))
        if char == "-":
            check_east(row, col + 1, step + 1)
        if char == "J":
            check_north(row, col + 1, step + 1)
        if char == "7":
            check_south(row, col + 1, step + 1)


def check_south(row, col, step):
    char = df[col][row + 1]
    if char == 'S':
        return
    if 'north' in pipe_rules[char]:
        if (row + 1, col, char) not in pipes_in_loop:
            pipes_in_loop[(row + 1, col, char)] = step + 1
        else:
            pipes_in_loop[(row + 1, col, char)] = min(pipes_in_loop[(row + 1, col, char)], (step + 1))
        if char == "|":
            check_south(row + 1, col, step + 1)
        if char == "L":
            check_east(row + 1, col, step + 1)
        if char == "J":
            check_west(row + 1, col, step + 1)


def check_west(row, col, step):
    char = df[col - 1][row]
    if char == 'S':
        return
    if 'east' in pipe_rules[char]:
        if (row, col - 1, char) not in pipes_in_loop:
            pipes_in_loop[(row, col - 1, char)] = step + 1
        else:
            pipes_in_loop[(row, col - 1, char)] = min(pipes_in_loop[(row, col - 1, char)], (step + 1))
        if char == "-":
            check_west(row, col - 1, step + 1)
        if char == "L":
            check_north(row, col - 1, step + 1)
        if char == "F":
            check_south(row, col - 1, step + 1)


num_rows, num_columns = df.shape

if s_row > 0:
    check_north(s_row, s_col, 0)
if s_col < num_columns:
    check_east(s_row, s_col, 0)
if s_row < num_rows:
    check_south(s_row, s_col, 0)
if s_col > 0:
    check_west(s_row, s_col, 0)

max_key = max(pipes_in_loop, key=pipes_in_loop.get)
print(pipes_in_loop[max_key])
