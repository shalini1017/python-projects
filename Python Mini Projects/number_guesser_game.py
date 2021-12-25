import random

start = 0

tries = 0

print("welcome to the number guesser game")


def take_user_input():
    top_of_range = input("Please type top of range: ")

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
    elif int(top_of_range) <= 0:
        print("Please type a number greater than 0 next time")
        quit()
    else:
        print("Please type a number next time")
        quit()

    return top_of_range


def play():
    top_of_range = take_user_input()
    random_number = random.randrange(top_of_range)
    print(random_number)

    user_guess = input(f"guess a number between {start} and {top_of_range} ")
    if int(user_guess) == random_number:
        print("You guessed it right!")
    else:
        print("you guessed it wrong!")
    play_again = input("You want to play again? (y/n) ")
    if play_again.lower() == "y":
        play()
    elif playing.lower() == "n":
        print("BYE")
    else:
        print("Enter only 'y' or 'n' ")
        quit()


playing = input("You want to play?(y/n) ")
if playing.lower() == "y":
    play()
elif playing.lower() == "n":
    print("BYE")
else:
    print("Enter only 'y' or 'n' ")
    quit()










