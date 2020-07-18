def get_table():
    table = "  1 | 2 | 3 \n____|___|____ \n  4 | 5 | 6 \n____|___|____ \n  7 | 8 | 9  \n    |   |   "
    return table


def get_win_conditions_list():
    win_conditions_list = [[1, 2, 3], [2, 5, 8], [3, 6, 9], [1, 4, 7], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]
    return win_conditions_list


def get_player1_sign():
    player1_sign = input("Plyaer 1: \nChoose between 'X' and 'O'! ").upper()
    if player1_sign == "X" or player1_sign == "O":
        return player1_sign
    else:
        print("Invalid input... Please choose 'X' or 'O'!")
        get_player1_sign()


def get_play2_sign(player1_sign):
    if player1_sign == "X":
        player2_sign = "O"
        print("So Player 2's sign is " + player2_sign + "!")
        return player2_sign
    else:
        player2_sign = "X"
        print("So Player 2's sign is " + player2_sign + "!")
        return player2_sign


def get_checklist(win_conditions_list):
    checklist = []
    for i in win_conditions_list:
        for w in i:
            checklist.append(w)
    checklist = list(set(checklist))
    return checklist


def get_player_input():
    player_input = input("Choose a field to mark! ")
    return player_input


def input_check(player_input, checklist):
    for i in range(len(checklist)):
        if player_input == str(checklist[i]):
            checklist.remove(checklist[i])
            return checklist
        else:
            print("Invalid input!")
            input_check(get_player_input(), checklist)
    return checklist


def set_mark_on_table(player_input, table, sign):
    table = table.replace(player_input, sign)
    return table


def add_sign_to_win_cons(win_conditions_list, player_input, sign):
    win_conditions_list = [[str(i).replace(player_input, sign) for i in win_con] for win_con in win_conditions_list]
    return win_conditions_list


#def win_check(win_conditions_list, sign):
 #   for i in win_conditions_list:
  #      for w in range(len(i) - 1):
   #         if i[w] == sign and i[w + 1] == sign and i[w + 2] == sign:
    #            print("Congratulations! " + sign + " wins!")
     #           quit()
