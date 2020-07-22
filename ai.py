import random
import menu


def defensive_instinct(checklist, win_conditions_list, sign, sign2):
    if checklist:
        defensive_input = str(random.choice(checklist))
        for i in win_conditions_list:
            if sign == i[0] and sign == i[1] and i[2] != sign2:
                defensive_input = str(i[2])
                return defensive_input
            elif sign == i[0] and sign == i[2] and i[1] != sign2:
                defensive_input = str(i[1])
                return defensive_input
            elif sign == i[1] and sign == i[2] and i[0] != sign2:
                defensive_input = str(i[0])
                return defensive_input
        return defensive_input
    else:
        print("No winner this time... C'mon, it's an easy game!")
        menu.menu()


def offensive_instinct(checklist, win_conditions_list, sign, sign2):
    if checklist:
        offensive_input = str(random.choice(checklist))
        for i in win_conditions_list:
            if sign2 == i[0] and sign2 == i[1] and i[2] != sign:
                offensive_input = str(i[2])
                return offensive_input
            elif sign2 == i[0] and sign2 == i[2] and i[1] != sign:
                offensive_input = str(i[1])
                return offensive_input
            elif sign2 == i[1] and sign2 == i[2] and i[0] != sign:
                offensive_input = str(i[0])
                return offensive_input
        return offensive_input
    else:
        defensive_instinct(checklist, win_conditions_list, sign, sign2)
