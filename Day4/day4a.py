txt_file_path = 'day4data.txt'
games = []

with open(txt_file_path, 'r') as file:
    for line in file:
        games.append(line.strip())

all_points = []

for game in games:
    numbers = game.split(":")[1].split("|")
    winning_numbers = numbers[0].strip().split()
    your_numbers = numbers[1].strip().split()
    game_points = 0
    for number in your_numbers:
        if number in winning_numbers:
            if game_points == 0:
                game_points = 1
            else:
                game_points *= 2
    all_points.append(game_points)

print(sum(all_points))
