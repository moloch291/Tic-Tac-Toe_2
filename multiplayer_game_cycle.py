import functions
import os
import time


def multiplayer_game_cycle():
    table = functions.get_table()
    win_conditions_list = functions.get_win_conditions_list()
    player1_sign = functions.get_player1_sign()
    player2_sign = functions.get_player2_sign(player1_sign)
    checklist = functions.get_checklist(win_conditions_list)
    for i in range(0, 9):
        if i % 2 == 0:
            print(table)
            print("Player 1:")
            player_input = functions.input_check(functions.get_player_input(), checklist)
            checklist = functions.remove_input_from_checklist(player_input, checklist)
            table = functions.set_mark_on_table(player_input, table, player1_sign)
            win_conditions_list = functions.add_sign_to_win_cons(win_conditions_list, player_input, player1_sign)
            functions.win_check(win_conditions_list, player1_sign, table)
            os.system('clear')
            time.sleep(1)
        else:
            print()
            print("Player 2:")
            player_input = functions.input_check(functions.get_player_input(), checklist)
            checklist = functions.remove_input_from_checklist(player_input, checklist)
            table = functions.set_mark_on_table(player_input, table, player2_sign)
            win_conditions_list = functions.add_sign_to_win_cons(win_conditions_list, player_input, player2_sign)
            functions.win_check(win_conditions_list, player2_sign, table)
            os.system('clear')
            time.sleep(1)
    print("No winner this time... C'mon, it's an easy game!")
