import json
users = r"D:\BUV university\Software Development\SDAM\w09\lab10\users.json"

#Fuction for main menu in terminal
def menu():
    print("Pick your option:\n1. New user\n2. Existing user\n3. Exit")
    #Prints out the choices and uses user input
    choice = input()
    if choice == "1":
        #Calls new_user function then prints out the menu again
        new_user()
        menu()
    elif choice == "2":
        #Calls existing_user function
        existing_user()
    elif choice == "3":
        #Exit choice
        print("Thank you. See you again.")
    else:
        #If input doesn't allign with predetermined inputs
        print("That's not a valid option. Try again.")
        menu()

#Checks if the user with a username already existed in the dictionary
def check_user_exist(username):
    try:
        with open(users, 'r') as file:
            usernames = json.load(file)
    except FileNotFoundError:
        usernames = {"Users": []}

    username_exists = any(user.get("Username") == username for user in usernames.get("Users", []))

    return username_exists

#Checks if the password from an existing user is correct with what is entered
def check_password(password):
    try:
        with open(users, 'r') as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {"Users": []}

    password_correct = any(user.get("Password") == password for user in passwords.get("Users", []))

    return password_correct

#Makes a new user with a username and a password and saves it in users.json
def new_user():
    #Makes a user template
    user = {"Username": "", "Password": ""}
    #User inputs a username, doesn't accept if the username already exists in users.json
    while True:
        username = input("Enter a username: ")
        #Calls check_user_exist function to check if the username exists already
        if check_user_exist(username):
            print("Username already exists")
        else:
            break
    #User inputs a password with at least 8 characters, doesn't start with a number and have no spaces in it
    print("Enter a password (at least 8 characters, no spaces, doesn't begin with a number):")
    while True:
        password = input()
        if " " in password:
            print("Password invalid. Try again.")
        elif len(password.strip()) < 8:
            print("Password invalid. Try again.")
        elif password[0].isdigit():
            print("Password invalid. Try again.")
        else:
            break
    #Requires the user to re-input the password, if it doesn't match it will keep prompting the user for it
    print("Re enter your password:")
    while True:
        re_password = input()
        if not re_password == password:
            print("Passwords don't match.")
        else:
            break
    
    #Saves both username and password int the user template
    user["Username"] = username
    user["Password"] = password

    #Saves the user as a new user in the users.json file
    with open(users,'r+') as file:
        file_data = json.load(file)
        file_data["Users"].append(user)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

    print("User {} has been created. Welcome {}.".format(username, username))

#Login to an existing user in users.json file
def existing_user():
    tries = 3
    while True:
        username = input("Enter your username: ")
        #Checks if the username is an existing one in users.json
        if not check_user_exist(username):
            print("Username doesn't exists")
        else:
            break
    
    while tries != 0:
        password = input("Enter your password: ")
        if not check_password(password):
            print("Password is incorrect. Try again.")
            tries -= 1
        else:
            print("Welcome in {}.".format(username))
            break

    if tries == 0:
        print("Wrong password entered 3 times. Terminating code.")

menu()