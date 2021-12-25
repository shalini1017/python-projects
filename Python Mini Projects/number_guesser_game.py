import random

STEP = 50

i = 0
tries = 0

print("welcome to the number guesser game")


def play():
    number = random.randint(i, i + STEP)
    #print(number)

    user_guess = input(f"guess a number between {i} and {i + STEP} ")
    if int(user_guess) == number:
        print("You guessed it right!")
    else:
        print("you guessed it wrong!")
    play_again = input("You want to play again? (y/n) ")
    if play_again == "y":
        play()


playing = input("You want to play?(y/n) ")
if playing.lower() == "y":
    play()










