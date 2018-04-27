
# for i in range(10):
#     print("i is now {}".format(i))
# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1
#
# availableExits = ["east", "north east", "south"]
#
# chosenExit = ""
# while chosenExit not in availableExits:
#     chosenExit = input("Please choose a direction: ")
#     if chosenExit == "quit":
#         print("Game Over")
#         break
#
# else:
#     print("Aren't you glad you got out of there?")

import random

highest = 10
answer = random.randint(1, highest)
i
print("Please guess a number between 1 and {}".format(highest))
guess = 0  # initialize to any number outside of the valid range

while guess != answer:
    guess = int(input())
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:  # guess must be greater than random number
        print("Please guess lower")
    else:
        print("Well done, you've guessed it")


