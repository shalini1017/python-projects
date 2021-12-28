import random

print("\n**** Welcome to the rock paper scissors game ****\n")
print("Here are the game winning rules:\n\n Rock vs paper-> paper wins\n\n Rock vs scissor-> Rock wins\n\n\
 paper vs scissor-> scissor wins.\n\n")

input_choices = ["rock", "paper", "scissor"]

print(f"select an option from the following:\n option 1: {input_choices[0]}\n\
 option 2: {input_choices[1]}\n option 3: {input_choices[2]}\n")

# print(f"input choices: {input_choices}")
print("select an option")


def take_user1_input():
    """
    Takes user1 input choice
    :return: user1 input choice
    """
    try:
        user1_input = int(input("Enter your choice: "))

        if 0 < user1_input <= 3:
            print(f"you chose {input_choices[user1_input-1]}")
        else:
            print("You chose an invalid option")
            quit()
        return user1_input

    except ValueError:
        print("Please select a numeric (1,2 or 3) option next time")
        quit()


def take_user2_input():
    """
    :return: user2 input choice.
    computer is user2 here.
    """
    user2_input = random.randint(1, 3)
    print(f"user2 chose {input_choices[user2_input-1]}")
    return user2_input


def play():
    """
    Defines the game rules and decides who wins by
    comparing the user1 and user2 input choices
    """
    user1_input = take_user1_input()
    user2_input = take_user2_input()
    input_dict = {"user1": user1_input, "user2": user2_input}

    if list(input_dict.values()) == [1, 2] or list(input_dict.values()) == [2, 1]:
        for key, val in input_dict.items():
            if val == 2:
                print(f"{key} wins")

    if list(input_dict.values()) == [1, 3] or list(input_dict.values()) == [3, 1]:
        for key, val in input_dict.items():
            if val == 1:
                print(f"{key} wins")

    if list(input_dict.values()) == [3, 2] or list(input_dict.values()) == [2, 3]:
        for key, val in input_dict.items():
            if val == 3:
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

