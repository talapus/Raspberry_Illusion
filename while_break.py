
import random

myScore = 1
while True:
    print('Your score so far is {}.'.format(myScore))
    print("Would you like to roll or quit?")
    ans = raw_input("Roll...")
    if ans.lower() == 'r':
        R = random.randint(1, 8)
        print("You rolled a {}.".format(R))
        myScore = R + myScore
    else:
        print("Now I'll see if I can break your score...")
        break