from functions import get_top_scores, play_game

user_name = input('Hi! What\'s your name? ')

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ").upper()

    if selection == "A":
        play_game(name=user_name)
    elif selection == "B":
        for score_dict in get_top_scores():
            print(
                "\t{0} finished the game with {1} attempts. The game was played on {2}"
                .format(
                    score_dict["player_name"],
                    score_dict["attempts"],
                    score_dict["date"].split('.')[0])
            )
    elif selection == "C":
        break
    else:
        print('Unknown command. Please enter A, B or C')

print('Igra je koncana')
