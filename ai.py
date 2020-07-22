import random


def choose_a_field(checklist, win_conditions_list, sign, sign2):
    player_input = str(random.choice(checklist))
    for i in win_conditions_list:
        if sign == i[0] and sign == i[1] and i[2] != sign2:
            player_input = str(i[2])
            return player_input
        elif sign == i[0] and sign == i[2] and i[1] != sign2:
            player_input = str(i[1])
            return player_input
        elif sign == i[1] and sign == i[2] and i[0] != sign2:
            player_input = str(i[0])
            return player_input
        elif sign2 == i[0] and sign2 == i[1] and i[2] != sign:
            player_input = str(i[2])
            return player_input
        elif sign2 == i[0] and sign2 == i[2] and i[1] != sign:
            player_input = str(i[1])
            return player_input
        elif sign2 == i[1] and sign2 == i[2] and i[0] != sign:
            player_input = str(i[0])
            return player_input
    return player_input
