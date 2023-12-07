txt_file_path = 'day4data.txt'
games = []

with open(txt_file_path, 'r') as file:
    for line in file:
        games.append(line.strip())

game_scores = {}
game_cards = {}

i = 1
for game in games:
    numbers = game.split(":")[1].split("|")
    winning_numbers = numbers[0].strip().split()
    your_numbers = numbers[1].strip().split()
    game_points = 0
    for number in your_numbers:
        if number in winning_numbers:
            game_points += 1
    game_scores[i] = game_points
    game_cards[i] = 1
    i += 1

for key, value in game_scores.items():
    for i in range(value):
        game_cards[key + i + 1] += 1 * game_cards[key]

total = sum(game_cards.values())

print(total)
