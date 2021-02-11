import random

secret = random.randint(1, 10)
st_poizkusa = 0

while True:
    st_poizkusa = st_poizkusa + 1

    guess = int(input("Guess the secret number (between 1 and 10): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number {0}. This was your {1} attempt."
              .format(secret, st_poizkusa))
        break
    elif guess > secret:
        print('Your attempt ({0}) is too high. This was your {1} attempt.'.format(guess, st_poizkusa))
    else:
        print("Your attempt ({0}) is too low. This was your {1} attempt.".format(guess, st_poizkusa))

print('Igra je koncana')
