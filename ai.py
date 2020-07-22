import random


def choose_a_field(checklist, win_conditions_list, sign):
    player_input = str(random.choice(checklist))
    for i in win_conditions_list:
        if sign == i[0] and sign == i[1] and i[2] != "O":
            player_input = str(i[2])
            return player_input
        elif sign == i[0] and sign == i[2] and i[1] != "O":
            player_input = str(i[1])
            return player_input
        elif sign == i[1] and sign == i[2] and i[0] != "O":
            player_input = str(i[0])
            return player_input

    return player_input
