# The program bellow allows the player to guess the
# the number as many time as he/she wants.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

import random


highest = 1000
answer = random.randint(1, highest)

user_input = int(input("Please enter a number between 1 and {0}: ".format(highest)))
numberOfGuesses = 0
while user_input != answer:
    if user_input == 0:
        print("You aborted the Game")
        break
    if user_input > answer:
        user_input = int(input("Please enter lower number: "))
    else:
        user_input = int(input("Please enter higher number: "))
    numberOfGuesses += 1
else:
    print("Congratulation, you spot the correct answer after {0} guess(es).".format(numberOfGuesses))
