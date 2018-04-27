import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you've guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it, first try!")
