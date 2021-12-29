master_pwd = input("Enter your master password")


def view_pwd():
    """
    View all username and passwords existing in pwd.txt file
    """
    with open("pwd.txt", 'r') as f:
        contents = f.read()
        print(contents)


def add_pwd():
    """
    Add new username and password to pwd.txt file
    """
    print("Enter your username and password you want to store")
    user_name = input("UserName: ")
    pwd = input("Password: ")
    with open("pwd.txt", 'a') as f:
        f.write(f"{user_name}, {pwd}\n")


while True:
    mode = input("You want to view your existing passwords or add a new one (add/view)? Press 'q' to quit.").lower().strip()
    if mode == "view":
        view_pwd()
        continue
    elif mode == "add":
        add_pwd()
        continue
    elif mode == "q":
        print("You chose to quit the application")
        break
    else:
        print("Invalid mode. Please select the valid mode")
        continue
