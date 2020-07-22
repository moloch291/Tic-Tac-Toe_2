import random
import menu


def defensive_and_offensive_instinct(checklist, win_conditions_list, sign, sign2):
    if checklist:
        defensive_input = str(random.choice(checklist))
        for i in win_conditions_list:
            if sign == i[0] and sign == i[1] and i[2] != sign2 or sign2 == i[0] and sign2 == i[1] and i[2] != sign:
                defensive_input = str(i[2])
                return defensive_input
            elif sign == i[0] and sign == i[2] and i[1] != sign2 or sign2 == i[0] and sign2 == i[2] and i[1] != sign:
                defensive_input = str(i[1])
                return defensive_input
            elif sign == i[1] and sign == i[2] and i[0] != sign2 or sign2 == i[1] and sign2 == i[2] and i[0] != sign:
                defensive_input = str(i[0])
                return defensive_input
        return defensive_input
    else:
        print("No winner this time... C'mon, it's an easy game!")
        menu.menu()
