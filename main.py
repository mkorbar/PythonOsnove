
# string
mood = input("What's your mood \"bro\" ")
age = int(input("what's your age"))

if mood == 'sad' or age >= 18:
    reason = input('why are you sad')
    if reason == 'corona':
        print('It will pass soon')
    print('Please don\'t cry')
elif mood == 'happy':
    print('I\'m happy that you\'re happy')
else:
    print("I don't understand you")

print("You're {0}".format(mood))


# # int, float
# birth_year = int(input("what's your birth year"))
# age = 2021-birth_year
# print("you're {0} years old".format(age))
#
# # boolean
# trenutnco_je_dan = False
# zelim_si_na_pivo_v_bar = True
#
# # None type
# prazna_vrednos = None
