import random
import json
import datetime


def get_score_list():
    with open('high_score.txt', 'r') as high_score_fp:
        return json.loads(high_score_fp.read())


def get_top_scores(count=3):
    sorted_scores = sorted(get_score_list(), key=lambda s: s['attempts'])
    return sorted_scores[:count]


def write_score_list(score_list):
    with open('high_score.txt', 'w') as high_score_fp:
        high_score_fp.write(json.dumps(score_list, indent=4))


def print_hint(guess, secret):
    if guess > secret:
        print('Your attempt ({0}) is too high.'.format(guess))
    else:
        print("Your attempt ({0}) is too low.".format(guess))


def play_game(name, hard_mode=False):
    st_poizkusa = 0
    secret = random.randint(1, 10)
    score_list = get_score_list()
    while True:
        st_poizkusa = st_poizkusa + 1

        guess = int(input("Guess the secret number (between 1 and 10): "))

        if guess == secret:
            print("You've guessed it - congratulations! It's number {0}. This was your {1} attempt."
                  .format(secret, st_poizkusa))
            game_data = {
                'date': str(datetime.datetime.now()),
                'player_name': name,
                'attempts': st_poizkusa
            }
            score_list.append(game_data)
            write_score_list(score_list)
            break
        else:
            if hard_mode:
                print("That's not correct, try again")
            else:
                print_hint(guess, secret)
