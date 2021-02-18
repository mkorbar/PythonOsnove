import json
import random
import datetime

secret = random.randint(1, 10)
st_poizkusa = 0

name = input('Hi! What\'s your name?')

with open('high_score.txt', 'r') as high_score_fp:
    score_list = json.loads(high_score_fp.read())
    print('Past results are:')
    score_list.sort()
    print(score_list)

while True:
    st_poizkusa = st_poizkusa + 1

    guess = int(input("Guess the secret number (between 1 and 10): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number {0}. This was your {1} attempt."
              .format(secret, st_poizkusa))
        game_data = {
            'time': str(datetime.datetime.now()),
            'player name': name,
            'score': st_poizkusa
        }
        score_list.append(game_data)

        with open('high_score.txt', 'w') as high_score_fp:
            high_score_fp.write(json.dumps(score_list, indent=4))

        break
    elif guess > secret:
        print('Your attempt ({0}) is too high. This was your {1} attempt.'.format(guess, st_poizkusa))
    else:
        print("Your attempt ({0}) is too low. This was your {1} attempt.".format(guess, st_poizkusa))

print('Igra je koncana')
