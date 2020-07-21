import singleplayer_game_cyle
import multiplayer_game_cycle


def menu():
    player_choice = input("Menu:\nChoose an option:\n1: Single-player mode\n2: Multiplayer mode\n3: Quit\n ")
    if player_choice == "1":
        singleplayer_game_cyle.single_player_game_cycle()
    elif player_choice == "2":
        multiplayer_game_cycle.multiplayer_game_cycle()
    elif player_choice == "3":
        print("Good bye!")
        quit()
    else:
        print("Invalid input!\nPlease type the number of an option in the menu and press ENTER!")
        menu()
