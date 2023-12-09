import pandas as pd

cards = "AKQJT98765432"
card_ranking = {}
for i in range(len(cards)):
    card_ranking[cards[i]] = len(cards) - i

txt_file_path = 'data.txt'
games = []

with open(txt_file_path, 'r') as file:
    for line in file:
        games.append(line.strip())
columns = ['cards', 'bid', 'scores', 'card1', 'card2', 'card3', 'card4', 'card5']
df = pd.DataFrame(columns=columns)

for game in games:
    cards = game.split()[0]
    bid = int(game.split()[1])
    card_count = {}
    card_ranks = []
    for card in cards:
        card_ranks.append(card_ranking[card])
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1
    max_amount = card_count[max(card_count, key=lambda k: card_count[k])]
    if max_amount == 5:
        score = 7
    elif max_amount == 4:
        score = 6
    elif max_amount == 3 and len(card_count) == 2:
        score = 5
    elif max_amount == 3:
        score = 4
    elif max_amount == 2 and len(card_count) == 3:
        score = 3
    elif max_amount == 2:
        score = 2
    else:
        score = 1
    df.loc[len(df.index)] = [cards, bid, score, card_ranks[0], card_ranks[1], card_ranks[2], card_ranks[3],
                             card_ranks[4]]

df_sorted = df.sort_values(by=['scores', 'card1', 'card2', 'card3', 'card4', 'card5']).reset_index(drop=True)
df_sorted.index += 1
df_sorted['result'] = df_sorted.index * df_sorted['bid']

print(sum(df_sorted['result'].values))
