import json
import os
import random
import time
import metmuseum

folder = "logindetails"
if not os.path.exists(folder):
    os.makedirs(folder)
print("Welcome to the game of cities")


def login():
    log = input("Do you have an account Y/N ?")
    if log.lower() == "n":
        signup()
    elif log.lower() == "y":
        print("Login to the game".center(50, "-"))
        user = input("What is your username? ")
        password = input("What is your password? ")
        try:
            with open(os.path.join(folder, user + ".json"), "r") as game:
                info = json.load(game)
            if info["username"] == user and info["password"] == password:
                print("Welcome to the game of cities ", user.title() + "!")
                #the game continues in main.py

                with open("current_player.json", "w") as file:
                    json.dump(info, file)
            else:
                print("Incorrect username or password, try again")
                login()
        except FileNotFoundError:
            print("\nWe can not find that account\nPlease try again\n")
            login()
    else:
        print("Please choose a valid option")
        login()


def signup():
    print("Account Setup".center(40, '*'))
    username = input("Please enter your Username: ")
    while True:
        password = input("Please enter your password: ")
        confirm = input("Please re enter password: ")
        if password == confirm:
            break
        else:
            print("Passward did not match")

    data = {}
    start = time.time()
    data['username'] = username
    data['password'] = password
    data['money'] = 100
    data['energy'] = 100
    data['bag'] = metmuseum.bagitems()
    data['start'] = start
    data['city'] = 0

    with open(os.path.join(folder, username + ".json"), "w") as infile:
        data = json.dump(data, infile)
    login()


login()
