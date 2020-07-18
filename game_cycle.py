import functions


def game_cycle():
    table = functions.get_table()
    win_conditions_list = functions.get_win_conditions_list()
    player1_sign = functions.get_player1_sign()
    player2_sign = functions.get_play2_sign(player1_sign)
    checklist = functions.get_checklist(win_conditions_list)
    print(table)
    for i in range(0, 10):
        if i % 2 != 0:
            player_input = functions.get_player_input()
            checklist = functions.input_check(player_input, checklist)
            table = functions.set_mark_on_table(player_input, table, player1_sign)
            win_conditions_list = functions.add_sign_to_win_cons(win_conditions_list, player_input, player1_sign)
            print(table)
        else:
            player_input = functions.get_player_input()
            checklist = functions.input_check(player_input, checklist)
            table = functions.set_mark_on_table(player_input, table, player2_sign)
            win_conditions_list = functions.add_sign_to_win_cons(win_conditions_list, player_input, player2_sign)
            print(table)
    print("No winner this time... C'mon, it's an easy game!")