import json
import urllib.request
import random as r
from termcolor import cprint
import login
from clearscreen import clear
import time
import hosts
import weather as w

time.sleep(2)
clear()

with open("current_player.json", "r") as file:
    details = json.load(file)

print(details)

url = "https://raw.githubusercontent.com/rashmijswl/Module-8---Escape-game/main/game.json"
request = urllib.request.urlopen(url)
response = json.loads(request.read())

choice = input("Do you want to [start] over or [continue]? ")
if choice.lower() == "start":
    city = 0
else:
    city = details["city"]

while True:
    clear()
    temperature = w.city_temp()

    print(
        f"You have CAD {details['money']}\nYou have {details['energy']}%\nYou have  {details['bag']} in bag"
    )
    if response[city]['win'] == 1:
        cprint(f"{response[city]['Story']}", "blue")
        break
    elif response[city]['lose'] == 1:
        print(f"{response[city]['Story']}")
        break

        print(f"\n{response[city]['Story']}")
    print(
        f"The temperature in this city is {round(temperature[0],2)} degree celsius"
    )
    print(f"\n{response[city]['Navigation']}")
    choice = int(input())
    if response[city]['host1'] == 1:
        print("THE HOST STANGER IS HERE TO MEET YOU")
        time.sleep(2)
        hosts.talk_to_host()

    if choice == 1 or (choice != 2 and choice != 3 and choice != 4):
        nextcity = response[city]['t1']
    elif choice == 2:
        nextcity = response[city]['t2']
    elif choice == 3:
        nextcity = response[city]['t3']
    else:
        nextcity = response[city]['t4']

    city = nextcity - 1
    details['city'] = city

    with open("current_player.json", "w") as file:
        details = json.dump(details, file)

    with open("current_player.json", "r") as file:
        details = json.load(file)
