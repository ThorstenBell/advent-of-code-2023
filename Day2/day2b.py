txt_file_path = 'day2data.txt'
lines_array = []

with open(txt_file_path, 'r') as file:
    for line in file:
        lines_array.append(line.strip())


def cube_power():
    results_array = []
    for row in lines_array:
        game = row.split(":")[1].split(";")
        max_blue = max_red = max_green = 0
        for hand in game:
            hand_results = hand.split(",")
            for hand_result in hand_results:
                colour = hand_result.split()[1]
                amount = int(hand_result.split()[0])
                if colour == 'red' and amount > max_red:
                    max_red = amount
                elif colour == 'green' and amount > max_green:
                    max_green = amount
                elif colour == 'blue' and amount > max_blue:
                    max_blue = amount
        power = max_red * max_green * max_blue
        results_array.append(power)
    print(sum(results_array))


cube_power()
