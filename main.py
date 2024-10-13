# This is a guess the number game
from random import randrange

random_num = randrange(1,20)
num_guesses = 0

print("I am thinking of a number between 1 and 20")
while num_guesses < 6:
    num_guesses += 1
    print("Take a guess.")
    user_input = int(input())
    if user_input < random_num:
        print("Your guess is too low.")
    elif user_input > random_num:
        print("Your guess is too high.")
    else:
        break

if user_input == random_num:
    print("Good Job! You guessed the number in", num_guesses, "guesses!")
else:
    print("Nope. The correct number was", random_num, ".")