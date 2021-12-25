import random

start = 0

print("welcome to the number guesser game")


def take_user_input():
    top_of_range = 0

    try:
        top_of_range = int(input("Please type top of range: "))
        if top_of_range <= 0:
            print("Please enter a positive number next time")
            quit()
    except ValueError:
        print("Oops! That is not a valid number. Try again..")
        quit()

    return top_of_range


def play():
    top_of_range = take_user_input()
    random_number = random.randrange(top_of_range)
    print(random_number)
    print(f"guess a number between {start} and {top_of_range}")
    tries = 0
    while tries < 5:
        tries += 1

        user_guess = input("guess: ")
        if int(user_guess) == random_number:
            print(f"You guessed it right! you took {tries} tries")
            break
        else:
            print(f"you guessed it wrong! you took {tries} tries")
            continue
    ask_play_again()


def ask_play_again():
    play_again = input("You want to play again? (y/n) ")
    if play_again.lower() == "y":
        play()
    elif play_again.lower() == "n":
        print("BYE BYE")
    else:
        print("Enter only 'y' or 'n'")
        ask_play_again()


playing = input("You want to play?(y/n) ")
if playing.lower() == "y":
    play()
elif playing.lower() == "n":
    print("BYE")
else:
    print("Enter only 'y' or 'n' ")
    quit()










