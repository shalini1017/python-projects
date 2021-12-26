import random

input_choices = ["rock", "paper", "scissors"]
print("Welcome to the rock paper scissors game")

print(f"input choices: {input_choices}")
print("select a choice from the given list")


def take_user1_input():
    """
    Takes user1 input choice
    :return: user1 input choice
    """
    user1_input = input("Enter your choice: ").lower()
    if user1_input not in input_choices:
        print("Invalid input, please select from the given list")
        quit()
    return user1_input


def take_user2_input():
    """
    :return: user2 input choice.
    computer is user2 here.
    """
    user2_input = random.choice(input_choices)
    return user2_input


def play():
    """
    Defines the game rules and decides who wins by
    comparing the user1 and user2 input choices
    """
    user1_input = take_user1_input()
    user2_input = take_user2_input()
    input_dict = {"user1": user1_input, "user2": user2_input}

    if list(input_dict.values()) == ["rock", "paper"] or list(input_dict.values()) == ["paper", "rock"]:
        for key, val in input_dict.items():
            if val == "paper":
                print(f"{key} wins")

    if list(input_dict.values()) == ["rock", "scissors"] or list(input_dict.values()) == ["scissors", "rock"]:
        for key, val in input_dict.items():
            if val == "rock":
                print(f"{key} wins")

    if list(input_dict.values()) == ["scissors", "paper"] or list(input_dict.values()) == ["paper", "scissors"]:
        for key, val in input_dict.items():
            if val == "scissors":
                print(f"{key} wins")

    if input_dict["user1"] == input_dict["user2"]:
        print("Tie")

    play_again()


def play_again():
    """
    Asks the user1 if he wants to play again.
    Acceptable inputs from user1 are 'y' or 'n'
    """
    playing = input("want to play again? (y/n): ").lower()
    if playing == "y":
        play()
    elif playing == "n":
        print("Bye Bye")
        quit()
    else:
        print("Invalid input, Enter 'y' or 'n'")


play()

